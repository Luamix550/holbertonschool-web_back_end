import ClassRoom from './0-classroom';

let arrayName = [];

function initializeRooms() {
  arrayName = [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
  return arrayName;
}

export default initializeRooms;
