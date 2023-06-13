#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2]);
if (isNaN(x))
{
	console.log("Missing number of occurrences");
}
else
{
	let j = 0;
	while (j < x)
	{
		let res = "C is fun";
		console.log(res);
		j++;
	}
}
