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
                    git branch: "mod/294", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install smmap2==2.0.4 --user
                pip2 install gitdb2==2.0.4 --user
                pip2 install gitpython==2.1.8 --user
                /usr/bin/python ./test/unit/git_class/gitmerge_init.py
                /usr/bin/python ./test/unit/git_class/gitmerge_detach_head.py
                /usr/bin/python ./test/unit/git_class/gitmerge_get_br_name.py
                /usr/bin/python ./test/unit/git_class/gitmerge_remove_branch.py
                /usr/bin/python ./test/unit/git_class/gitmerge_create_gitrepo.py
                /usr/bin/python ./test/unit/git_class/gitmerge_set_remote.py
                /usr/bin/python ./test/unit/git_class/gitmerge_is_remote.py
                /usr/bin/python ./test/unit/git_class/gitmerge_process_dirty.py
                /usr/bin/python ./test/unit/git_class/gitmerge_process_untracked.py
                /usr/bin/python ./test/unit/git_class/gitmerge_is_dirty.py
                /usr/bin/python ./test/unit/git_class/gitmerge_is_untracked.py
                /usr/bin/python ./test/unit/git_class/gitmerge_git_fetch.py
                /usr/bin/python ./test/unit/git_class/gitmerge_rename_br.py
                /usr/bin/python ./test/unit/git_class/gitmerge_git_co.py
                /usr/bin/python ./test/unit/git_class/gitmerge_priority_merge.py
                /usr/bin/python ./test/unit/git_class/gitmerge_git_pu.py
                /usr/bin/python ./test/unit/git_class/gitmerge_commits_diff.py
                /usr/bin/python ./test/unit/git_class/gitmerge_is_commits_ahead.py
                /usr/bin/python ./test/unit/git_class/gitmerge_is_commits_behind.py
                /usr/bin/python ./test/unit/git_class/gitmerge_is_remote_branch.py
                /usr/bin/python ./test/unit/git_class/gitmerge_get_dirty.py
                /usr/bin/python ./test/unit/git_class/gitmerge_get_untracked.py
                /usr/bin/python ./test/unit/git_class/gitclass_init.py
                /usr/bin/python ./test/unit/git_class/gitclass_create_repo.py
                /usr/bin/python ./test/unit/git_class/gitclass_create_init.py
                /usr/bin/python ./test/unit/git_class/gitclass_create_cmd.py
                /usr/bin/python ./test/unit/git_class/gitconfig_init.py
                /usr/bin/python ./test/unit/git_class/gitconfig_get_email.py
                /usr/bin/python ./test/unit/git_class/gitconfig_get_user.py
                /usr/bin/python ./test/unit/git_class/gitconfig_set_email.py
                /usr/bin/python ./test/unit/git_class/gitconfig_set_user.py
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
