#!groovy

currentBuild.result = "SUCCESS"
pipeline {
    agent {
	 label "SG-SALESFORCE-CI"
	}
	stages{
        stage("Test start for UI automation classical") {
            when { environment name: 'Model', value: 'classical' }
            options {
                retry(1) 
                }
            steps {
                echo "test on ${params.Env}"
                powershell "& ./scripts/UI_run_classical.ps1 ${params.Env}"
                }
			}
        stage("Test start for UI automation lighting") {
            when { environment name: 'Model', value: 'lighting' }
            options {
                retry(1) 
                }
            steps {
                echo "test on ${params.Env}"
                powershell "& ./scripts/UI_run_lighting.ps1 ${params.Env}"
                }
			}
			
			}
    post {
        always {
            junit '/**/Result/*.xml'
                
                
            emailext (
              subject: "${currentBuild.result}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
              to: "sunny.yu2@ef.com",
              body: """<p>${currentBuild.result}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
              attachmentsPattern: '\\**\\Result\\*.png',
              attachLog:true,
            )      
                            
        }	
            }
        }