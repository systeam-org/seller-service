#!/usr/bin/env groovy
node {
  def TestService = 'TestService'

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

  stage('Run Test Cases') {
    build_ddr = build job: "${TestService}",
      parameters: [
        string(name: 'ServiceName', value: "Seller")

      ]
  }
}