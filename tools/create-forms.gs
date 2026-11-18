/**
 * Life Builders: creates the three website forms and one response spreadsheet.
 * Paste into a new project at script.google.com, choose createLifeBuildersForms, click Run.
 * Safe to read: it only creates new files in your Drive. It does not change or delete anything.
 */
const LIFE_BUILDERS_FOLDER_ID = '1TmHQhgU44fHv5nDM2gp-NQbG2EsqKPPc'; // Life Builders folder in Drive

function createLifeBuildersForms() {
  const folder = DriveApp.getFolderById(LIFE_BUILDERS_FOLDER_ID);
  const sheet = SpreadsheetApp.create('Life Builders Form Responses');
  DriveApp.getFileById(sheet.getId()).moveTo(folder);

  const forms = [buildMentorshipForm(), buildStoryForm(), buildContactForm()];
  const lines = ['Responses spreadsheet: ' + sheet.getUrl()];
  forms.forEach(function (form) {
    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());
    form.setAllowResponseEdits(false);
    form.setShowLinkToRespondAgain(false);
    form.setCollectEmail(false);
    form.setAcceptingResponses(true);
    if (typeof form.setPublished === 'function') form.setPublished(true); // newer forms start unpublished
    DriveApp.getFileById(form.getId()).moveTo(folder);
    lines.push(form.getTitle() + ': ' + form.getPublishedUrl() + ' | edit: ' + form.getEditUrl());
  });
  Logger.log(lines.join('\n'));
}

function buildMentorshipForm() {
  const f = FormApp.create('Life Builders Mentorship Application');
  f.setDescription(
    'A free, 90-day virtual mentorship for men 18 and older. It takes about 10 minutes. ' +
    'Our team reads every application and follows up personally.\n\n' +
    'Life Builders mentorship is not counseling or therapy. If you are in crisis, call or text 988 (Suicide & Crisis Lifeline).');
  f.setConfirmationMessage('Thank you for applying. Our team reads every application and will follow up with you personally.');

  f.addSectionHeaderItem().setTitle('About you');
  f.addTextItem().setTitle('Full name').setRequired(true);
  f.addTextItem().setTitle('Email').setRequired(true)
    .setValidation(FormApp.createTextValidation().requireTextIsEmail().build());
  f.addTextItem().setTitle('Phone').setRequired(true);
  f.addTextItem().setTitle('City and state').setRequired(true);
  f.addMultipleChoiceItem().setTitle('Age range').setRequired(true)
    .setChoiceValues(['18 to 24', '25 to 34', '35 to 44', '45 to 54', '55 or older']);
  f.addMultipleChoiceItem().setTitle('Marital status')
    .setChoiceValues(['Single', 'Married', 'Separated or divorced', 'Widowed', 'Prefer not to say']);
  f.addMultipleChoiceItem().setTitle('Do you have children?').setChoiceValues(['Yes', 'No']);

  f.addPageBreakItem().setTitle('Where you are');
  f.addParagraphTextItem().setTitle("What's going on in your life right now that made you apply?").setRequired(true);
  f.addCheckboxItem().setTitle('Where do you feel most stuck? Choose any that apply.').setRequired(true)
    .setChoiceValues(['Faith', 'Marriage', 'Fatherhood', 'Work or career', 'Health', 'Purpose and direction', 'Habits or addiction'])
    .showOtherOption(true);
  f.addParagraphTextItem().setTitle('What do you want to be different 90 days from now?').setRequired(true);
  f.addMultipleChoiceItem().setTitle('How would you describe your faith right now?')
    .setChoiceValues(['Growing and active', 'A believer, but inconsistent', 'Exploring', 'Not sure']);

  f.addPageBreakItem().setTitle('Commitment');
  f.addMultipleChoiceItem().setTitle('Mentorship runs 90 days and meets virtually. Can you commit to meeting with your mentor regularly for 90 days?')
    .setRequired(true).setChoiceValues(['Yes', 'I have questions first']);
  f.addCheckboxItem().setTitle('What times usually work best for you?')
    .setChoiceValues(['Weekday mornings', 'Weekday lunch', 'Weekday evenings', 'Weekends']);
  f.addMultipleChoiceItem().setTitle('How did you hear about Life Builders?').setRequired(true)
    .setChoiceValues(['The Standard podcast', 'Saints Crown', 'A friend or family member', 'My church', 'Social media'])
    .showOtherOption(true);
  f.addParagraphTextItem().setTitle('Anything else we should know?');
  f.addCheckboxItem().setTitle('Agreement').setRequired(true)
    .setChoiceValues(['I understand the Life Builders team will review my application, and mentorship is free once I am approved.']);
  return f;
}

function buildStoryForm() {
  const f = FormApp.create('Share Your Story with Life Builders');
  f.setDescription(
    'Has The Standard podcast helped you? Tell us. It takes about 5 minutes.\n\n' +
    'Your story stays private. We will only share it publicly if you give permission below.');
  f.setConfirmationMessage('Thank you for sharing your story. It stays private unless you gave us permission to share it.');

  f.addTextItem().setTitle('First name').setRequired(true);
  f.addTextItem().setTitle('Email').setHelpText("We'll only use this to follow up about your story.").setRequired(true)
    .setValidation(FormApp.createTextValidation().requireTextIsEmail().build());
  f.addTextItem().setTitle('City and state');
  f.addMultipleChoiceItem().setTitle('How long have you listened to The Standard?')
    .setChoiceValues(['Less than 3 months', '3 to 12 months', 'More than a year']);
  f.addParagraphTextItem().setTitle('Where were you when you started listening? What were you facing?').setRequired(true);
  f.addParagraphTextItem().setTitle('What message, idea or moment made a difference?').setRequired(true);
  f.addParagraphTextItem().setTitle("What's different now in you, your marriage, your family or your work?").setRequired(true);
  f.addMultipleChoiceItem().setTitle('May we share your story publicly?').setRequired(true)
    .setChoiceValues(['Yes, with my first name', 'Yes, but keep it anonymous', 'No, keep it private']);
  f.addMultipleChoiceItem().setTitle('May we contact you to follow up?').setRequired(true)
    .setChoiceValues(['Yes', 'No']);
  return f;
}

function buildContactForm() {
  const f = FormApp.create('Contact Life Builders');
  f.setDescription("Questions about mentorship, giving or the podcast? Send us a message and we'll get back to you.");
  f.setConfirmationMessage("Thanks for reaching out. We'll get back to you soon.");

  f.addTextItem().setTitle('Name').setRequired(true);
  f.addTextItem().setTitle('Email').setRequired(true)
    .setValidation(FormApp.createTextValidation().requireTextIsEmail().build());
  f.addTextItem().setTitle('Phone (optional)');
  f.addMultipleChoiceItem().setTitle("What's this about?").setRequired(true)
    .setChoiceValues(['Mentorship', 'Sharing a story', 'Giving, including stock or IRA gifts', 'The Standard podcast', 'Volunteering or becoming a mentor'])
    .showOtherOption(true);
  f.addParagraphTextItem().setTitle('Message').setRequired(true);
  return f;
}
