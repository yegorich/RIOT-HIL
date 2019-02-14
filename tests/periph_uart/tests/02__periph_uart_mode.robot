*** Settings ***
Suite Setup         Run Keywords    Reset DUT and PHILIP
...                                 DUT Must Have Periph UART Application
Test Setup          Run Keywords    Reset DUT and PHILIP
...                                 DUT Must Have Periph UART Application

Resource            periph_uart.keywords.txt
Resource            api_shell.keywords.txt

Variables           test_vars.py

Force Tags          periph  uart

*** Test Cases ***
Even Parity 8 Bits
    PHILIP.Setup Uart		parity=${UART_PARITY_EVEN}
    API Call Should Succeed     Uart Init
    API Call Should Succeed     Uart Mode             data_bits=8   parity="E"   stop_bits=1
    API Call Should Succeed     Uart Send String      ${SHORT_TEST_STRING}
    Should Be Equal             ${RESULT['data'][0]}  ${SHORT_TEST_STRING}
    API Call Should Succeed     Uart Mode             data_bits=8   parity="O"   stop_bits=1
    API Call Should Timeout     Uart Send String      ${SHORT_TEST_STRING}

Odd Parity 8 Bits
    PHILIP.Setup Uart		parity=${UART_PARITY_ODD}
    API Call Should Succeed     Uart Init
    API Call Should Succeed     Uart Mode             data_bits=8   parity="O"   stop_bits=1
    API Call Should Succeed     Uart Send String      ${SHORT_TEST_STRING}
    Should Be Equal             ${RESULT['data'][0]}  ${SHORT_TEST_STRING}
    API Call Should Succeed     Uart Mode             data_bits=8   parity="E"   stop_bits=1
    API Call Should Timeout     Uart Send String      ${SHORT_TEST_STRING}

Even Parity 7 Bits
    PHILIP.Setup Uart		parity=${UART_PARITY_EVEN}   databits=${UART_DATA_BITS_7}
    API Call Should Succeed     Uart Init
    API Call Should Succeed     Uart Mode             data_bits=7   parity="E"   stop_bits=1
    API Call Should Succeed     Uart Send String      ${SHORT_TEST_STRING}
    Should Be Equal             ${RESULT['data'][0]}  ${SHORT_TEST_STRING}
    API Call Should Succeed     Uart Mode             data_bits=7   parity="O"   stop_bits=1
    API Call Should Timeout     Uart Send String      ${SHORT_TEST_STRING}

Odd Parity 7 Bits
    PHILIP.Setup Uart		parity=${UART_PARITY_ODD}   databits=${UART_DATA_BITS_7}
    API Call Should Succeed     Uart Init
    API Call Should Succeed     Uart Mode             data_bits=7   parity="O"   stop_bits=1
    API Call Should Succeed     Uart Send String      ${SHORT_TEST_STRING}
    Should Be Equal             ${RESULT['data'][0]}  ${SHORT_TEST_STRING}
    API Call Should Succeed     Uart Mode             data_bits=7   parity="E"   stop_bits=1
    API Call Should Timeout     Uart Send String      ${SHORT_TEST_STRING}

Two Stop Bits
    PHILIP.Setup Uart		parity=${UART_PARITY_ODD}
    API Call Should Succeed     Uart Init
    API Call Should Succeed     Uart Mode             data_bits=8   parity="N"   stop_bits=2
    API Call Should Succeed     Uart Send String      ${TEST_STRING_FOR_STOP_BITS}
    Should Be Equal             ${RESULT['data'][0]}  ${TEST_STRING_FOR_STOP_BITS}
    API Call Should Succeed     Uart Mode             data_bits=8   parity="N"   stop_bits=1
    API Call Should Timeout     Uart Send String      ${TEST_STRING_FOR_STOP_BITS}
