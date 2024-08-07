import redis from 'redis';

const client = redis.createClient();

function setNewSchool(schoolName,value) {
    client.set(schoolName,value,redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName,(err,res) => {
        console.log(res);
    })
}

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');