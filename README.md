# brandonv.io

## Portfolio Projects

- [trackerp.xyz](#trackerp)
- [fuzzle.xyz](#fuzzlexyz)
- [reallo.xyz](#realloxyz)
- [rythm.cc](#rythmcc)
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
