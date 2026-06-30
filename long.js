// Load environment variables
import dotenv from 'dotenv';
dotenv.config();

const apiKey = process.env.MY_API_KEY;

// Example fetch request passing the key as a Bearer token
async function fetchData() {
  const response = await fetch('https://amirisgoat597.github.io/catgpt/', {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    }
  });
  const data = await response.json();
  console.log(data);
}
