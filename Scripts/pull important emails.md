function getGlutenFreeOrders() {
  var label = GmailApp.getUserLabelByName("Pay Stub"); // Ensure this label exists
  
  if (label === null) {
    Logger.log("Label not found! Please check the label name.");
    return;
  }
  
  var threads = label.getThreads();
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Orders") || SpreadsheetApp.getActiveSpreadsheet().insertSheet("Orders");
  
  // Clear previous data
  sheet.clear();
  
  // Set header
  sheet.appendRow(["Date", "Sender", "Subject", "Body"]);

  threads.forEach(thread => {
    var messages = thread.getMessages();
    messages.forEach(message => {
      var date = message.getDate();
      var sender = message.getFrom();
      var subject = message.getSubject();
      var body = message.getBody().replace(/<[^>]+>/g, ''); // Remove HTML tags

      // Limit body length to the first 100 characters
      body = body.length > 100 ? body.substring(0, 100) + '...' : body;

      // Append each message data to the sheet
      sheet.appendRow([date, sender, subject, body]);
    });
  });
}