import java.io.*
import java.lang.*
import java.math.BigDecimal
import java.math.BigInteger
import java.net.*
import java.util.*
import groovy.lang.*
import groovy.util.*

node ("Lab01") {
    stage('Checkout SCM') {
            cleanWs()
            checkout scm
            updateGitlabCommitStatus name: 'build', state: 'pending'
        }
        
        // stage('Flash SD card') {
        //    def Flash = load("flashSD.groovy")
        //    Flash("ubuntucore_backup.img","a")
        //    echo 'Done flash'
        //}
        stage('Turn On power board') {
            def On = load("relayon.groovy")
            echo 'Done Turn on'
        }
        stage('Turn On power board') {
            def Off = load("relayoff.groovy")
            echo 'Done turn off'
        }
        stage('check status board') {
            def Status = load("statusboard.groovy")
            Status("test28.py")
            echo 'Done check status'
        }
         stage('Run test')
        {
            sh (returnStdout: true, label: "Run test command",
            script: '''
                #!/usr/bin/env bash
                chmod +x shunit2-xml/src/shell/shunit2*
                chmod +x testsuite_01.sh
                sudo apt-get install -y bc
                bash testsuite_01.sh > testsuite_01_result.xml
            ''')
            
            testlogs = findFiles excludes: '', glob: 'testcase_*.log'
            testlogs.each { log ->
                def logdata = readFile "${log}"
                println "${log}:"
                println "${logdata}"
            }
            junit 'testsuite_01_result.xml'
            updateGitlabCommitStatus name: 'build', state: 'success'
        }
}

