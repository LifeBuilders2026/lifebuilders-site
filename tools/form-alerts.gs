/**
 * Life Builders form alerts.
 *
 * Emails every new form response (mentorship, story, contact) to the
 * people in RECIPIENTS, with all the answers in the body and Reply-To set
 * to the person who filled out the form.
 *
 * Setup (one time):
 *   1. Paste this file into the same Apps Script project as create-forms.gs
 *      (or a new project at script.google.com), signed in as the account
 *      that owns the "Life Builders Form Responses" sheet.
 *   2. Pick setupLifeBuildersAlerts in the function menu and click Run.
 *   3. Approve the permissions Google asks for.
 *
 * To change who gets alerts, edit RECIPIENTS and run setup again.
 */

const RESPONSES_SHEET_ID = '1nlsSmdbaB8SmuCbhZr-tLfEhmiu52IHLiTV5cXkohPc';

const RECIPIENTS = [
  'preston@saintscrown.com',
  'connect@tombrittingham.com',
];

// Tab name in the response sheet -> subject line prefix.
const FORM_LABELS = {
  'Mentorship Applications': 'New mentorship application',
  'Story Submissions': 'New story submission',
  'Contact Messages': 'New contact message',
};

function setupLifeBuildersAlerts() {
  ScriptApp.getProjectTriggers()
    .filter(function (t) { return t.getHandlerFunction() === 'onLifeBuildersSubmit'; })
    .forEach(function (t) { ScriptApp.deleteTrigger(t); });

  ScriptApp.newTrigger('onLifeBuildersSubmit')
    .forSpreadsheet(RESPONSES_SHEET_ID)
    .onFormSubmit()
    .create();

  Logger.log('Alerts on. New responses will email: ' + RECIPIENTS.join(', '));
}

function onLifeBuildersSubmit(e) {
  const sheet = e.range.getSheet();
  const tab = sheet.getName();
  const label = FORM_LABELS[tab] || 'New Life Builders form response';

  const lastCol = sheet.getLastColumn();
  const headers = sheet.getRange(1, 1, 1, lastCol).getDisplayValues()[0];
  const values = sheet.getRange(e.range.getRow(), 1, 1, lastCol).getDisplayValues()[0];

  let name = '';
  let email = '';
  const rows = [];
  headers.forEach(function (h, i) {
    const v = values[i] || '';
    const key = h.toLowerCase();
    if (!name && key.indexOf('name') !== -1) name = v;
    if (!email && key.indexOf('email') !== -1) email = v;
    rows.push([h, v]);
  });

  const sheetUrl = 'https://docs.google.com/spreadsheets/d/' + RESPONSES_SHEET_ID +
    '/edit#gid=' + sheet.getSheetId();
  const subject = label + (name ? ': ' + name : '');

  const html =
    '<div style="font-family:Arial,sans-serif;font-size:14px;color:#1c2340">' +
    '<p style="font-size:16px;font-weight:bold">' + esc(subject) + '</p>' +
    '<table cellpadding="6" style="border-collapse:collapse">' +
    rows.map(function (r) {
      return '<tr><td style="vertical-align:top;color:#8a6a2f;font-weight:bold;' +
        'border-bottom:1px solid #ede8db">' + esc(r[0]) + '</td>' +
        '<td style="border-bottom:1px solid #ede8db;white-space:pre-wrap">' +
        esc(r[1]) + '</td></tr>';
    }).join('') +
    '</table>' +
    '<p><a href="' + sheetUrl + '">Open the ' + esc(tab) + ' tab</a></p>' +
    (email ? '<p style="color:#666">Reply to this email to reach ' +
      esc(name || 'them') + ' directly.</p>' : '') +
    '</div>';

  const text = subject + '\n\n' +
    rows.map(function (r) { return r[0] + ': ' + r[1]; }).join('\n') +
    '\n\n' + sheetUrl;

  const msg = {
    to: RECIPIENTS.join(','),
    subject: subject,
    body: text,
    htmlBody: html,
    name: 'Life Builders',
  };
  if (email && email.indexOf('@') !== -1) msg.replyTo = email;

  MailApp.sendEmail(msg);
}

function esc(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
