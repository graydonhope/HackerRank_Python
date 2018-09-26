from collections import Counter
class AvailableRooms:
	numberOfMembers, roomNumberList = int(input()),list(map(int, input().split()))
	roomNumberTotal = len(roomNumberList)
	numberOfGroups = roomNumberTotal / (numberOfMembers - 1) 
	instancesOfRooms = Counter(roomNumberList)
	leastCommon = instancesOfRooms.most_common()[-1]
	print(leastCommon[0])