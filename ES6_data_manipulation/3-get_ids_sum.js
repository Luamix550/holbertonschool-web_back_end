export default function getStudentIdsSum(arrayStudents) {
  return arrayStudents.reduce((accumulator, number) => accumulator + number.id, 0);
}
