import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup () {
  const result = Promise.all([uploadPhoto(), createUser()]);
  result.then((result) => {
    console.log(`${result[0].body} ${result[1].firstName} ${result[1].lastName}`);
  });

  return result.catch(() => {
    console.log('Signup system offline');
  });
}
