#!/usr/bin/env groovy
node {
  def TestServiceJob = 'TestService'
  def BuildContainerJob = 'BuildContainer'

  stage('Checkout from Git') {
  		checkout ([
  		$class: 'GitSCM',
  		branches: [[name: '*/master']],
  		extensions: [
  				[$class: 'CleanCheckout']
  		],
  		userRemoteConfigs: [[credentialsId: 'admin', url: 'https://github.com/systeam-org/seller-service']]
  		])
  }

  stage('Execute API Tests') {
    build_service = build job: "${TestServiceJob}",
      parameters: [
        string(name: 'ServiceName', value: "Seller")

      ]
  }

  stage('Build Docker Image') {
    build_ddr = build job: "${BuildContainerJob}"
  }

}