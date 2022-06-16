pipeline {
  agent any
  stages {
    stage ("build") {
      steps {
        echo 'building application.....'
      }
    }
    stage ("test") {
      // you can specify condition to satisfy before the steps are executed
      when {
        expression {
          BRANCH_NAME =='jenkins-addition' || BRANCH_NAME =='main'
        }
      }
      steps {
        echo 'testing application.....'
      }
    }
    stage ("deploy") {
      steps {
        echo 'deploying application.....'
      }
    }
  }
}
