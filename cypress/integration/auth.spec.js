describe("Authentication", () => {
  it("Can sign up and log in", () => {
    let emailAddress = "test-user-" + Date.now() + "@example.com";
    cy.visit("/");
    cy.contains("Sign Up").click();
    cy.contains("Email")
      .click()
      .type(emailAddress);
    cy.contains("Password")
      .click()
      .type("Some Complicated Password");
    cy.contains("button", "Sign Up").click();
    cy.contains("Successfully signed in");
    cy.contains("Sign Out").click();
    cy.contains("button", "Sign Out").click();
    cy.contains("You have signed out");
    cy.contains("Log In").click();
    cy.contains("Email")
      .click()
      .type(emailAddress);
    cy.contains("Password")
      .click()
      .type("Some Complicated Password");
    cy.contains("button", "Sign In").click();
    cy.contains("Successfully signed in");
  });
});
