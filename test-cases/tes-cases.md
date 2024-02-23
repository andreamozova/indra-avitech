# Feature: Email 
 
## Scenario: User logging in and out
    
**Given** User is on gmail main page
**When** user clicks on `sign in` button  
**Then** sign in modal is visible 

**When** user fills in correct email in email field  
**And** user click on `next` button  
**Then** password modal is visible  
**And** correct account is visible in modal  

**When** user fills in correct password   
**And** user click on `next` button  
**Then** user is successfully signed in  

**When** user clicks on account button  
**And** clicks on `sign out` button  
**Then** user is successfully signed out
 
## Scenario: User is able to send email
    
**Given** User is on gmail main page
**When** user clicks on `sign in` button  
**Then** sign in modal is visible 

**When** user fills in correct email in email field  
**And** user click on `next` button  
**Then** password modal is visible  
**And** correct account is visible in modal

**When** user fills in correct password  
**And** user click on `next` button  
**Then** user is successfully signed in

**When** user clicks on `compose` button  
**Then** modal for writing new email is visible

**When** user clicks on `To` button within email modal  
**And** chooses first contact  
**And** clicks on `insert` button  
**Then** receiver input field is correctly prefilled

**When** user clicks on `send` button  
**Then** new email modul is not visible  
**And** success message is visible

**When** user clicks on account button  
**And** clicks on `sign out` button  
**Then** user is successfully signed out
 
## Scenario: User is able to send email with attached file
    
**Given** User is on gmail main page
**When** user clicks on `sign in` button  
**Then** sign in modal is visible 

**When** user fills in correct email in email field  
**And** user click on `next` button  
**Then** password modal is visible  
**And** correct account is visible in modal

**When** user fills in correct password   
**And** user click on `next` button  
**Then** user is successfully signed in

**When** user clicks on `compose` button  
**Then** modal for writing new email is visible

**When** user clicks on `To` button within email modal  
**And** chooses first contact  
**And** clicks on `insert` button  
**Then** receiver input field is correctly prefilled

**When** user clicks on `attach file` button  
**And** chooses a file  
**Then** attached file is visible in email body

**When** user clicks on `send` button  
**Then** new email modul is not visible  
**And** success message is visible

**When** user clicks on account button  
**And** clicks on `sign out` button  
**Then** user is successfully signed out