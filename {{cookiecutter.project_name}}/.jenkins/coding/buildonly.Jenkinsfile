pipeline {
  agent {
    docker {
      image 'biggates/poetry:1.8.2-py3.10-slim'
      args '-e PATH=/root/.local/bin/:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
    }
  }

  stages {
    stage('检出') {
      steps{
        checkout([
          $class: 'GitSCM',
          branches: [[name: env.GIT_BUILD_REF]],
          userRemoteConfigs: [[
            url: env.GIT_REPO_URL,
            credentialsId: env.CREDENTIALS_ID
          ]]
        ])
      }
    }

    stage('安装依赖项') {
      steps {
        withCredentials([usernamePassword(credentialsId:'44404aed-5649-4b01-966d-8f009f01fa56',usernameVariable:'CODING_USER_NAME',passwordVariable:'CODING_PASSWORD')]) {
          sh 'poetry config http-basic.eaphone-protected $CODING_USER_NAME $CODING_PASSWORD'
          sh 'poetry install --with ci,dev{% if cookiecutter.include_pytest -%},testing{% endif %}{% if cookiecutter.include_sphinx -%},docs{% endif %}'
        }
      }
    }

    stage('编译 package') {
      steps {
        sh 'poetry build'
      }
    }

    {% if cookiecutter.include_pytest -%}
    stage('运行单元测试') {
      steps {
        sh 'poetry run pytest'
      }
      post {
        always {
          junit 'reports/test-result.xml'

          codingHtmlReport(
            name: 'cov-report',
            tag: 'test',
            path: 'htmlcov',
            des: '代码覆盖率报告',
            entryFile: 'index.html'
          )
        }
      }
    }
    {% endif %}

    {% if cookiecutter.include_sphinx -%}
    stage('编译文档') {
      steps {
        dir ('./docs') {
          sh 'poetry run sphinx-build -M html source build'
        }
      }
    }
    {% endif %}
  }
}
