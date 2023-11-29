import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the serve');
});

client.on('error', (error) => {
	console.error(`Redis client not connected to the server: ${error}`);
});

const getAsync = promisify(client.get).bind(client);
async function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
	const reply = await getAsync(schoolName);
	console.log(reply);
}
