*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new group
    ${old_list}=   Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=   Get Group List
    Append To list  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Delete group
    ${list}=   Get Group List
    Verify Group List Is Not Empty  ${list}
    ${old_list}=   Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  Get From List  ${old_list}  ${index}
    Delete Group  ${group}
    ${new_list}=   Get Group List
    Remove Values From List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Modify group
    ${list}=   Get Group List
    Verify Group List Is Not Empty  ${list}
    ${old_list}=   Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  Get From List  ${old_list}  ${index}
    ${id_group}=  Get Group id  ${group}
    Remove Values From List  ${old_list}  ${group}
    ${group_new_data}=  New Group For Modify  name2  header2  footer2  ${id_group}
    Modify Group  ${group}  ${group_new_data}
    ${new_list}=   Get Group List
    Append To list  ${old_list}  ${group_new_data}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Add new contact
    ${old_list}=   Get Contact List
    ${contact}=  New Contact  firstname1  lastname1  address1
    Create Contact  ${contact}
    ${new_list}=   Get Contact List
    Append To list  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${list}=   Get Contact List
    Verify Contact List Is Not Empty  ${list}
    ${old_list}=   Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=   Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Modify contact
    ${list}=   Get Contact List
    Verify Contact List Is Not Empty  ${list}
    ${old_list}=   Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    ${id_contact}=  Get Contact id  ${contact}
    Remove Values From List  ${old_list}  ${contact}
    ${contact_new_data}=  New Contact For Modify  firstname2  lastname2  address2  ${id_contact}
    Modify Contact  ${contact}  ${contact_new_data}
    ${new_list}=   Get Contact List
    Append To list  ${old_list}  ${contact_new_data}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}