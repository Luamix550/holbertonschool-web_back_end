export default function updateUniqueItems(itemMap) {
    if (typeof itemMap !== 'object' || itemMap === null || Array.isArray(itemMap)) {
        throw new Error('Cannot process');
    }

    Object.entries(itemMap).forEach(([item, quantity]) => {
        if (quantity === 1) {
            itemMap[item] = 100;
        }
    });

    return itemMap;
}