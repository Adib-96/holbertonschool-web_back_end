export default function getListStudentIds(arrayOfObj) {
  if (!Array.isArray(arrayOfObj)) {
    return [];
  }
  return arrayOfObj.map((ele) => ele.id);
}
