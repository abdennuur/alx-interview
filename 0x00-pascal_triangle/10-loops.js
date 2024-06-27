export default function appendToEachArrayValue(array, appendString) {
  const nwArr = [];
  for (const value of array) {
    nwArr.push(appendString + value);
  }

  return nwArr;
}
