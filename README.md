# Room Assignment During Pandemic
## Description
Suppose n people lined up waiting for consultations. Person i needs q<sub>i</sub> minutes for their consultation, where q<sub>i</sub> is a positive integer. There are t available rooms and each room can be used for a maximum of L minutes. The goal is to assign the people to the rooms so that the first n<sub>1</sub> go to room 1,the next n<sub>2</sub> go to room 2, ..., the last n<sub>t</sub> go to room t.
During the pandemic, to minimize contact, gaps between successive people using the same room should be maximized. The algorithm written with dynamic programming finds the room assignment (ie. n<sub>1</sub>, n<sub>2</sub>, ..., n<sub>t</sub>) to maximize the minimum gap between any two people.

![alt text](https://github.com/ellensong99/DP-RoomAssignmentCovid-MaxGap/blob/main/image.jpeg?raw=true)
 
## Usage
```bash
python roomAssignMaxGap.py sample.in
```
## Example
### Sample Input
  - Line 1: n, t, L, three integers separated by one space, where n is the number of poeple, t is the number of room, L is the maximum minutes a room can be used.
  - Line 2: n integers, q<sub>1</sub>, q<sub>2</sub>, ..., q<sub>n</sub> separated by one space, where q<sub>i</sub> is the amount of minutes person i need for consultation.
```bash
6 2 120
10 30 40 20 80 10
```

### Sample Output
  - Line 1: the optimal value of the smallest gap between any pair of people that are scheduled consecutively in the same room.
  - Line 2: n<sub>1</sub>, n<sub>2</sub>, ..., n<sub>t</sub>, optimized room assignment by assigning n<sub>1</sub> people to room 1, the next n<sub>2</sub> people to room 2, and so on.
```bash
6.66667
4 2
```

