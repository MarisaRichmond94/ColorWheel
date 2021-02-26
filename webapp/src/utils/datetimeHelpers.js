export const getTimeInMilliseconds = minutes => {
  const now = new Date().getTime();
  return now + (minutes * 60 * 1000);
};
