class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        # Format: (position, hoursNeeded)
        arrivals = [(pos, (target - pos) / speed[idx]) for idx, pos in enumerate(position)]
        # Sort based on position
        arrivals = sorted(arrivals, key=lambda x: x[0], reverse=True)

        fleetStack = deque()

        # print(f"[^^^] Arrivals: {arrivals}")

        for newArrival in arrivals:
            if len(fleetStack) == 0:
                fleetStack.append(newArrival)
                continue
            
            # print(f"[^^^^^] processing for newArrival: {newArrival}")
            
            # TODO: I might need a while loop here later.
            differentFleet = True
            for pendingIdx in range(len(fleetStack) - 1, -1, -1):
                pendingArrival = fleetStack[pendingIdx]
                blockedNew = newArrival[0] < pendingArrival[0] and newArrival[1] < pendingArrival[1]
                blockedPending = newArrival[0] > pendingArrival[0] and newArrival[1] > pendingArrival[1]
                similarArrival = newArrival[1] == pendingArrival[1]

                if blockedNew or blockedPending or similarArrival:
                    differentFleet = False
                    if blockedPending: # Replace with the blocker
                        fleetStack[pendingIdx] = newArrival
                    break
            
            if differentFleet: 
                fleetStack.append(newArrival)
            
            # print(f"[^^^^^] fleetStack condition post-processing: {fleetStack}")

        # print(f"[^^^] Final fleet: {fleetStack}")
        return len(fleetStack)

    def carFleetV2(self, target: int, position: List[int], speed: List[int]) -> int: # Failed on target=10, position=[0,4,2], speed=[2,1,3]

        # Format: (position, hoursNeeded)
        arrivals = [(pos, (target - pos) / speed[idx]) for idx, pos in enumerate(position)]
        fleetStack = deque()

        print(f"[^^^] Arrivals: {arrivals}")

        for newArrival in arrivals:
            if len(fleetStack) == 0:
                fleetStack.append(newArrival)
                continue
            
            print(f"[^^^^^] processing for newArrival: {newArrival}")
            
            # TODO: I might need a while loop here later.
            differentFleet = True
            for pendingIdx in range(len(fleetStack) - 1, -1, -1):
                pendingArrival = fleetStack[pendingIdx]
                blockedNew = newArrival[0] < pendingArrival[0] and newArrival[1] < pendingArrival[1]
                blockedPending = newArrival[0] > pendingArrival[0] and newArrival[1] > pendingArrival[1]
                similarArrival = newArrival[1] == pendingArrival[1]

                if blockedNew or blockedPending or similarArrival:
                    differentFleet = False
                    break
            
            if differentFleet: 
                fleetStack.append(newArrival)
            
            print(f"[^^^^^] fleetStack condition post-processing: {fleetStack}")

        print(f"[^^^] Final fleet: {fleetStack}")
        return len(fleetStack)

    def carFleetV1 (self, target: int, position: List[int], speed: List[int]) -> int: # Failed on target=100, position=[0,2,4], speed=[4,2,1]
        # Simulation 1
        #
        # position = [1,4]
        # speed = [3,2]
        # target = [10]
        # car 1: [1, 4, 7, 10] (3 per hour)
        # car 2: [4, 6, 8, 10] (2 per hour)
        # Result: 1 fleet, since car 1 and car 2 on the same position
        # Hour array: [ (10 - 1) / 3 , (10 - 4) / 2] = [3, 3]

        # Simulation 2
        #
        # position = [4, 1, 0, 7]
        # speed = [2, 2, 1, 1]
        # target = 10
        # 
        # Positions per hour
        # 1: [6, 3, 1, 8] -> 4 fleet
        # 2: [8, 5, 2, 9] -> 4 fleet
        # 3: [10, 7, 3, 10] -> 3 fleet
        # 4: [10, 9, 4,  10] -> 3 fleet
        # 5: [10, 10, 4,  10] -> 3 fleet, since the second arrived late
        # ... 10: [10, 10, 4,  10] -> 3 fleet, since the third arrived late

        # Hour array: [ (10 - 4) / 2 , (10 - 1) / 2, (10 - 0) / 1, (10 - 1) / 2, (10 - 7) / 1] = [3, 4.5, 10, 3] -> 3 fleet

        # So we need to consider how many hours til the car arrived at the target.
        # TODO: Consider how to represent the car that catched-up with the car on front of it.

        # Simulation 3
        #
        # target = 12
        # position = [10, 8, 0, 5, 3]
        # speed = [2, 4, 1, 1, 3]
        #
        # Positions per hour
        #
        # hour 1 = [12, 12, 1, 6, 6] -> 3 fleet (12 raeched, 6 on the way)
        # hour 2 = [12, 12, 2, 7, 9] -> not happening. 3 cannot go past 5.
        # CORRECTED hour 2 = [12, 12, 2, 7, 7] -> still 3 fleets.
        # hour 3 = [12, 12, 3, 8, 8] -> still 3 fleets.
        # ... hour 7 = [12, 12, 7, 12, 12]
        # ... hour 12 = [12, 12, 12, 12, 12]
        #
        # So... monotonic stack instead of set?
        # hour array = [(12 - 10)/ 2, (12 - 8) / 4, (12 - 0) / 1, (12 - 5) / 1, (12 - 3) / 3] = [1, 1, 12, 7, 3]
        # Fleet representation: [1, 12, 7]
        #
        # Not enough, we need to have the initial position to represent the order in this one-lane highway.
        # so, arrival array instead of hour array?
        # stucture: (initial position, est. arrival hour)
        # arrivalArray = [ (10, 1) , (8, 1) , (0 , 12) , (5, 7) , (3, 3) ]
        # This way, we can tell that (5, 7) blocks the (3, 3) from overlapping it.
        # Fleet representation: [(10, 1) , (0, 12) , ( 5, 7)]

        # Format: (position, hoursNeeded)
        arrivals = [(pos, (target - pos) / speed[idx]) for idx, pos in enumerate(position)]
        fleetStack = deque()

        print(f"[^^^] Arrivals: {arrivals}")

        for newArrival in arrivals:
            if len(fleetStack) == 0:
                fleetStack.append(newArrival)
                continue
            
            # TODO: I might need a while loop here later.
            differentFleet = True

            # Find reasons to not put the newArrival to the stack
            for pendingArrival in fleetStack:
                arrivingTogether = newArrival[1] == pendingArrival[1]
                combinedFleet = newArrival[1] < pendingArrival[1] and newArrival[0] < pendingArrival[0]
                
                if arrivingTogether or combinedFleet:
                    print(f"[^^^^^] Rejecting newArrival: {newArrival} after compared to pendingArrival: {pendingArrival}")
                    differentFleet = False
                    break

            if differentFleet:
                fleetStack.append(newArrival)

        print(f"[^^^] Final fleet: {fleetStack}")
        return len(fleetStack)
