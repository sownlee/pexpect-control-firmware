#!/bin/bash

suite() {
  suite_addTest testcase_02
}

testcase_02() {
  python test28.py | tee test28.log || true
  [[ $(cat test28.log) != *failed* ]]
}

oneTimeSetUp(){ :; }

setUp(){ :; }

oneTimeTearDown(){ :; }

tearDown(){ :; }

. shunit2-xml/src/shell/shunit2
