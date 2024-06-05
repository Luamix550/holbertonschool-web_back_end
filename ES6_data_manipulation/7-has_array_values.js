export default function hasValuesFromArray(set, array) {
  array.forEach(element => {
    if (!set.has(element)) {
      return false;
    }
  });
  return true;
}