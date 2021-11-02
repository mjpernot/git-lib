pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install smmap2==2.0.4 --user
                pip2 install gitpython==2.1.8 --user
                pip2 install gitdb==0.6.4 --user
                pip2 install gitdb2==2.0.4 --user
                ./test/unit/git_class/gitmerge_init.py
                ./test/unit/git_class/gitmerge_detach_head.py
                ./test/unit/git_class/gitmerge_get_br_name.py
                ./test/unit/git_class/gitmerge_remove_branch.py
                ./test/unit/git_class/gitmerge_create_gitrepo.py
                ./test/unit/git_class/gitmerge_set_remote.py
                ./test/unit/git_class/gitmerge_is_remote.py
                ./test/unit/git_class/gitmerge_process_dirty.py
                ./test/unit/git_class/gitmerge_process_untracked.py
                ./test/unit/git_class/gitmerge_is_dirty.py
                ./test/unit/git_class/gitmerge_is_untracked.py
                ./test/unit/git_class/gitmerge_git_fetch.py
                ./test/unit/git_class/gitmerge_rename_br.py
                ./test/unit/git_class/gitmerge_git_co.py
                ./test/unit/git_class/gitmerge_priority_merge.py
                ./test/unit/git_class/gitmerge_git_pu.py
                ./test/unit/git_class/gitmerge_commits_diff.py
                ./test/unit/git_class/gitmerge_is_commits_ahead.py
                ./test/unit/git_class/gitmerge_is_commits_behind.py
                ./test/unit/git_class/gitmerge_is_remote_branch.py
                ./test/unit/git_class/gitmerge_get_dirty.py
                ./test/unit/git_class/gitmerge_get_untracked.py
                ./test/unit/git_class/gitclass_init.py
                ./test/unit/git_class/gitclass_create_repo.py
                ./test/unit/git_class/gitclass_create_init.py
                ./test/unit/git_class/gitclass_create_cmd.py
                ./test/unit/git_class/gitconfig_init.py
                ./test/unit/git_class/gitconfig_get_email.py
                ./test/unit/git_class/gitconfig_get_user.py
                ./test/unit/git_class/gitconfig_set_email.py
                ./test/unit/git_class/gitconfig_set_user.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'art-svc-highpoint-dev'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/git-lib/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/git-lib/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/git-lib/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
    post {
        always {
            cleanWs disableDeferredWipeout: true
        }
    }
}
