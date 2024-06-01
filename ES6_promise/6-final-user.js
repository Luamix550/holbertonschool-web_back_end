import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [
    signUpUser(firstName, lastName),
    uploadPhoto(fileName)
  ];

  return Promise.allSettled(promises).then((results) => {
    return results.map((result) => {
      let value;
      if (result.status === 'fulfilled') {
        value = result.value;
      } else {
        value = result.reason;
      }
      return {
        status: result.status,
        value: value
      };
    });
  });
}
