#!/usr/bin/env groovy
node {
  def TestService = 'TestService'

  stage('Build Codebase') {
    build_ddr = build job: "${TestService}",
      parameters: [
        "ServiceName" : "Seller"
      ]
  }
}