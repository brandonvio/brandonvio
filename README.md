# brandonv.io

Greetings. My career experience so far has been mostly fullstack software engineering. However, throughout my career I've been involved in many other aspects of system delivery. My first tech job was with **Arcadia Software** who built the software that ran Qzar (at the time being the largest lazer tag franchise in the country). Part of my role was to configure the system for each new lazer tag center. This included installing the OS and the respective software for all 5 computers that ran the center, as well as networking the computers and validating connectivity and operations. Another highlight is building out and migrating all operational servers to a Hyper-V cluster for **Sgt Grit Marine Specialities** on top of a large Dell SAN for high availability. I also built out several CI/CD processes for companies such as **Broadlane** and **Crossmark** using CruiseControl.NET.

Moving forward I'm focusing in on **Solution Architecture** and **DevOps** culture esp. as relates to cloud and **AWS**. I want to be a part of the digitial transformation that is changing the very nature of organizations around the world. My goal is to build amazing systems that provide transformative value.

## LinkedIn Profile Highlights

- 3 AWS Certfications
- 1 Udemy and 3 Linux Academy Certifications for Course Completion
- 3 Microsoft Certifcations (expired)
- 22 Recommendations from former supervisors and colleagues.
- Over 120 skill endorsements across a broad spectrum of technologies.
- [Link to my LinkedIn profile](https://www.linkedin.com/in/brandonvicedomini/)
- [Link to my resume](https://github.com/brandonvio/brandonvio/blob/master/documents/BrandonVicedomini-Resume.pdf)

## NSS Overview

NSS is a system I worked on during my time at **American Fidelity**. NSS is the name of the integration systems for a larger product called FFSolutions. NSS processed hundreds of files every day, each file containing thousands of policy records. A robust ETL process esued for each record. The following document contains screenshots of the application. All of the screens and processes I personally designed, developed and supported.

[NSS Overview Document](https://github.com/brandonvio/brandonvio/blob/master/documents/NSS-Overview.pdf)

## Lonza MAST

**Lonza** is a freelance client I have been working with. Part of my work with the MAST team at Lonza has been to implement devops processes for the MAST Client Service application. As such I built out an Azure DevOps pipeline for the application for continuous integration. I've also implemented code coverage reporting and have begun the process of increasing the code coverage for the application. [Screenshots of the pipeline](https://github.com/brandonvio/brandonvio/tree/master/documents/lonza).

# Portfolio Projects

These are projects I've worked on for about the last 6 months. Some of these projects started out as coding challenges and were built out into a full functioning application. Rythm.cc started out as an idea to do machine learning using financial data and turned into a Jenkins/Kubernetes exercise. Each project is using CI/CD and is hosted in live environment on AWS or Azure.

- [trackerp.xyz](#trackerp) | a purchase tracking app | serverless | iac | hosted on AWS
- [fuzzle.xyz](#fuzzlexyz) | a blogging app | docker, ecs, mongodb | hosted on AWS
- [reallo.xyz](#realloxyz) | a real estate application | lambda, graphql, rds | Hosted on AWS
- [rythm.cc](#rythmcc) | a fintech tool | hosted on Kubernetes on Azure (AKS)
# trackerp

[github repo](https://github.com/brandonvio/trackerp)

Lightweight purchase tracking. Serverless. Built with care on AWS with Lambda, DynamoDB and Terraform.

Access the running application here:  
[trackerp](https://d2lq101g4g5eoi.cloudfront.net/)

## architecture - front end

- React - front end framework
- AWS S3 - static website hosting
- AWS Route53 - dns service
- AWS CloudFront - content distribution
- AWS Certificate Manager - SSL certificate
- Terraform - infrastructure as code
- Jenkins - CI/CD

## architecture - back end

- NodeJS - javascript runtime
- AWS Lambda - function as a service
- AWS API Gateway - api service
- DynamoDB - serverless nosql database service
- Terraform - infrastructure as code
- Jenkins - CI/CD

![Architecture](https://raw.githubusercontent.com/brandonvio/trackerp/master/docs/arch.png)

![Alt text](https://raw.githubusercontent.com/brandonvio/purchase-tracker-ioc/master/docs/PurchaseTracker04.png "Workstation screenshot...")

![Alt text](https://raw.githubusercontent.com/brandonvio/purchase-tracker-ioc/master/docs/PurchaseTracker03.png "Workstation screenshot...")

![Alt text](https://raw.githubusercontent.com/brandonvio/purchase-tracker-ioc/master/docs/PurchaseTracker05.png "Workstation screenshot...")

![Alt text](https://raw.githubusercontent.com/brandonvio/purchase-tracker-ioc/master/docs/PurchaseTracker02.png "Workstation screenshot...")

![Alt text](https://raw.githubusercontent.com/brandonvio/purchase-tracker-ioc/master/docs/image12.png "Workstation screenshot...")

![Alt text](https://raw.githubusercontent.com/brandonvio/purchase-tracker-ioc/master/docs/image13.png "Workstation screenshot...")

![Alt text](https://raw.githubusercontent.com/brandonvio/purchase-tracker-ioc/master/docs/image14.png "Workstation screenshot...")
# fuzzle.xyz

Lightweight blogging. Built with care on AWS and MongoDB.

Access the running application here:  
[https://fuzzle.xyz](https://fuzzle.xyz)

## architecture - front end | [fuzzle-app](https://github.com/brandonvio/fuzzle-app)

- React - front end framework
- AWS S3 - static website hosting
- AWS Route53 - domain hosting
- AWS CloudFront - content distribution
- AWS Certificate Manager - SSL certificate
- Jenkins - continuous integration/continuous delivery

## architecture - back end | [fuzzle-api](https://github.com/brandonvio/fuzzle-api)

- NodeJS - javascript runtime
- Docker - containerization
- AWS ECS - AWS container orchestration
- AWS API Gateway | HTTP API - api service
- MongoDB on Atlas - serverless nosql database service
- Jenkins - continuous integration/continuous delivery

![Architecture](https://raw.githubusercontent.com/brandonvio/fuzzle-app/master/public/images/arch.png "Architecture")

![Architecture](https://raw.githubusercontent.com/brandonvio/fuzzle-app/master/public/images/screenshot01.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/fuzzle-app/master/public/images/screenshot02.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/fuzzle-app/master/public/images/screenshot03.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/fuzzle-app/master/public/images/screenshot04.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/fuzzle-app/master/public/images/screenshot05.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/fuzzle-app/master/public/images/screenshot06.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/fuzzle-app/master/public/images/screenshot07.png)
# reallo.xyz

This is the repository for a reallo.xyz. A estate application I built to use as a portfolio project and showcase proficiency as a AWS Solutions Architect and Fullstack Software Engineer.

Access the running application here:  
[https://reallo.xyz](https://reallo.xyz)

username/password = reallo/reallo

## architecture - front end | [reallo-app](https://github.com/brandonvio/reallo-app)

- React - front end framework
- Redux - state management
- Formik - form management
- react-bootstrap - bootstrap responsive theme
- react-dropzone - file upload library
- AWS S3 - static website hosting
- AWS Route53 - domain hosting
- AWS CloudFront - content distribution
- AWS Certificate Manager - SSL certificate
- AWS CodeBuild - continuous integration and deployment
- AWS CodePipeline - continuous integration and deployment

## architecture - back end | [reallo-api](https://github.com/brandonvio/reallo-api)

- node.js - javascript runtime
- GraphQL - api layer
- Apollo Server - GraphQL server for node.js
- knex - data access layer
- AWS Lambda - serverless execution environment
- AWS API Gateway - api into lambda function
- AWS S3 - property image storage via S3 presigned urls
- AWS MySQL RDS - database server
- AWS CodeBuild - continuous integration and deployment
- AWS CodePipeline - continuous integration and deployment

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/arch.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot01.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot02.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot03.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot04.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot05.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot06.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot07.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot08.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot09.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot10.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/reallo-app/master/public/images/screenshot11.png)
## [rythm.cc](http://app.rythm.cc)

Forex, Crypto and Stock application. Running on a Kubernetes cluster in Azure. API integrations with [Oanda](https://www.oanda.com/us-en/), [IEX Cloud](https://iexcloud.io/) and [TradingView](https://www.tradingview.com/).

## Architecture

### Static Website

[rythm-app](https://github.com/brandonvio/rythm-app "rythm-app - Github")

- ReactJS running in Docker on Kubernetes.
- Socket.io used for realtime stream price data.
- [TradingView](https://www.tradingview.com/HTML5-stock-forex-bitcoin-charting-library/?library=cloud-widget) charts.

### API

[rythm-api](https://github.com/brandonvio/rythm-app "rythm-api - Github")

- NodeJS running in Docker on Kubernetes.
- Socket.io used for realtime stream price data.
- [Oanda API](https://developer.oanda.com/rest-live-v20/introduction/) integration.
- [IEX Cloud API](https://iexcloud.io/) integration.

### Microservices

[rythm-matrix](https://github.com/brandonvio/rythm-matrix "rythm-api - Github")

- Python microservice used to listen to HTTP stream of pricing data from Oanda.

### Data

- MongoDB running in VM on Azure. Pricing data stream via RabbitMQ. Data caching with Redis.

![Architecture](https://raw.githubusercontent.com/brandonvio/rythm-matrix/master/documentation/images/arch.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/rythm-matrix/master/documentation/images/screenshot01.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/rythm-matrix/master/documentation/images/screenshot02.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/rythm-matrix/master/documentation/images/screenshot03.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/rythm-matrix/master/documentation/images/screenshot06.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/rythm-matrix/master/documentation/images/screenshot04.png)

![Architecture](https://raw.githubusercontent.com/brandonvio/rythm-matrix/master/documentation/images/screenshot05.png)
