#!/usr/bin/env groovy
node {
  def TestService = 'TestService'

  stage('Run Test Cases') {
    build_ddr = build job: "${TestService}",
      parameters: [
        "ServiceName" : "Seller"
      ]
  }
}