#!/usr/bin/env groovy
node {
  def TestServiceJob = 'TestSellerService'
  def BuildContainerJob = 'BuildContainer'
  def GitOrganization = "systeam-org"
  def ServiceGitRepo = "seller-service"
  def DockerHubOrganization = "systeamorg"
  def ServiceDockerHubRepo = "seller-service"


  stage('Checkout from Git') {
  		checkout ([
  		$class: 'GitSCM',
  		branches: [[name: '*/master']],
  		extensions: [
  				[$class: 'CleanCheckout']
  		],
  		userRemoteConfigs: [[credentialsId: 'admin', url: "https://github.com/${GitOrganization}/${ServiceGitRepo}"]]
  		])
  }


  stage('Execute API Tests') {
    build_service = build job: "${TestServiceJob}"
  }

  stage('Build Docker Image') {
    build_ddr = build job: "${BuildContainerJob}",
    parameters: [
        string(name: 'GitOrganization', value: "${GitOrganization}"),
        string(name: 'ServiceGitRepo', value: "${ServiceGitRepo}"),
        string(name: 'DockerHubOrganization', value: "${DockerHubOrganization}"),
        string(name: 'ServiceDockerHubRepo', value: "${ServiceDockerHubRepo}")
      ]
  }

}