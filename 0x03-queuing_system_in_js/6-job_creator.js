const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
	phoneNumber: '1234567890',
	message: 'This is a notification message.',
};

const notificationJob = queue.create('push_notification_code', jobData);

notificationJob.on('complete', () => {
	console.log('Notification job complete');
});

notificationJob.on('failed', () => {
	console.log('Notification job failed');
});

notificationJob.save((err) => {
	if (!err) {
		console.log(`Notification job created: ${notificationJob.id}`);
	}
});
