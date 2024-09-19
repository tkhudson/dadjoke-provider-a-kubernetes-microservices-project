# Dad Joke Provider

In this project, we've built a Dad Joke Provider application using a microservices architecture and deployed it on a Kubernetes cluster. This project serves as an excellent introduction to containerization, microservices, and Kubernetes orchestration. 

## Future plans
I am currently in the stage to deploy this into a portfolio website and host it on AWS. This will replace my current portfolio website located at https://tylerkhudson.com.

## Explore the Project
Feel free to explore the project's code, architecture, and deployment details.

### To deploy the project:
You will need to get the backend joke services up and running. That is the joke, user, and api-gateway services. I have deployed it locally on my machine with minikube but if you would like to try this out yourself without kubernetes then to do so, open a seperate terminal for each service and run the following commands:
```
./start_apiservice.sh
./start_jokeservice.sh
./start_userservice.sh
```

#### Frontend Deployment
Then all thats needed is to deploy the frontend with the following command:
```
npm start
```

### Cheers!
Tyler