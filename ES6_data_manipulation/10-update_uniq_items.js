export default function updateUniqueItems(itemMap) {
    if (!(itemMap instanceof Map)) {
        throw new Error('Cannot process')
    }
    Object.entries(itemMap).forEach(([item, quantity]) => {
        if (quantity === 1) {
            itemMap[item] = 100;
        }
    });

    return itemMap;
}