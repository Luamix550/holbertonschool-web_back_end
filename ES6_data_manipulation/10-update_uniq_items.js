export default function updateUniqueItems(itemMap) {
  if (!(itemMap instanceof Map)) {
    throw new Error('Cannot process')
  }
  itemMap.forEach((item, quantity) => {
    if (item === 1) {
      itemMap.set(quantity, 100)
   }
  });
return itemMap;
}
