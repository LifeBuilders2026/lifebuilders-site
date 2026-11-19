/* Life Builders site forms: step navigation, validation, and posting
   answers into the matching Google Form. */
(function () {
  var EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function fieldsIn(scope) {
    return Array.prototype.slice.call(scope.querySelectorAll('.field'));
  }

  function setError(field, msg) {
    var el = field.querySelector('.field-error');
    if (!msg) {
      field.classList.remove('invalid');
      if (el) el.remove();
      return;
    }
    field.classList.add('invalid');
    if (!el) {
      el = document.createElement('p');
      el.className = 'field-error';
      field.appendChild(el);
    }
    el.textContent = msg;
  }

  function checkField(field) {
    if (field.classList.contains('group')) {
      var boxes = field.querySelectorAll('input[type=radio], input[type=checkbox]');
      var picked = Array.prototype.some.call(boxes, function (b) { return b.checked; });
      if (field.getAttribute('data-required') === '1' && !picked) {
        setError(field, 'Please choose an option.');
        return false;
      }
      var other = field.querySelector('input[value="__other_option__"]');
      if (other && other.checked) {
        var txt = field.querySelector('.other-text');
        if (!txt.value.trim()) {
          setError(field, 'Please fill in "Other".');
          return false;
        }
      }
      setError(field, '');
      return true;
    }
    var input = field.querySelector('input, textarea');
    var val = input.value.trim();
    if (input.required && !val) {
      setError(field, 'This is required.');
      return false;
    }
    if (val && input.type === 'email' && !EMAIL.test(val)) {
      setError(field, 'Please enter a valid email address.');
      return false;
    }
    setError(field, '');
    return true;
  }

  function checkScope(scope) {
    var ok = true;
    var first = null;
    fieldsIn(scope).forEach(function (f) {
      if (!checkField(f)) {
        ok = false;
        if (!first) first = f;
      }
    });
    if (first) {
      first.scrollIntoView({ behavior: 'smooth', block: 'center' });
      var focusable = first.querySelector('input, textarea');
      if (focusable) focusable.focus({ preventScroll: true });
    }
    return ok;
  }

  function init(form) {
    var wrap = form.closest('.lb-form-wrap');
    var steps = Array.prototype.slice.call(form.querySelectorAll('.form-step'));
    var markers = Array.prototype.slice.call(form.querySelectorAll('.form-steps li'));
    var errorBox = form.querySelector('.form-error');
    var current = 0;

    function show(i) {
      steps.forEach(function (s, n) { s.hidden = n !== i; });
      markers.forEach(function (m, n) {
        m.classList.toggle('active', n === i);
        m.classList.toggle('done', n < i);
      });
      current = i;
      wrap.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    form.addEventListener('click', function (e) {
      if (e.target.closest('[data-next]')) {
        if (checkScope(steps[current])) show(current + 1);
      } else if (e.target.closest('[data-back]')) {
        show(current - 1);
      }
    });

    // Clear an error as soon as the person fixes it.
    form.addEventListener('input', function (e) {
      var f = e.target.closest('.field');
      if (f && f.classList.contains('invalid')) checkField(f);
    });
    form.addEventListener('change', function (e) {
      var f = e.target.closest('.field');
      if (e.target.classList && e.target.classList.contains('other-text')) return;
      if (f && f.classList.contains('invalid')) checkField(f);
    });
    // Typing in "Other" selects that option.
    form.addEventListener('focusin', function (e) {
      if (e.target.classList.contains('other-text')) {
        var box = e.target.parentNode.querySelector('input[value="__other_option__"]');
        if (box && box.type === 'radio') box.checked = true;
        if (box && box.type === 'checkbox' && !box.checked) box.checked = true;
      }
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      errorBox.hidden = true;
      if (!checkScope(form)) return;
      var button = form.querySelector('button[type=submit]');
      var done = wrap.querySelector('.form-done');
      function finish() {
        form.hidden = true;
        done.hidden = false;
        done.focus();
        done.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      // Honeypot: real people never fill this in.
      if (form.querySelector('input[name=website]').value) { finish(); return; }

      var data = new URLSearchParams();
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.name === 'website' || el.disabled) return;
        if ((el.type === 'radio' || el.type === 'checkbox') && !el.checked) return;
        if (el.classList.contains('other-text')) {
          var picked = el.parentNode.querySelector('input[value="__other_option__"]');
          if (!picked || !picked.checked) return;
        }
        if (el.type !== 'radio' && el.type !== 'checkbox' && !el.value.trim()) return;
        data.append(el.name, el.value.trim());
      });
      var pages = parseInt(form.getAttribute('data-pages'), 10) || 1;
      if (pages > 1) {
        var hist = [];
        for (var i = 0; i < pages; i++) hist.push(i);
        data.append('pageHistory', hist.join(','));
      }

      button.disabled = true;
      button.textContent = 'Sending...';
      fetch(form.getAttribute('data-action'), { method: 'POST', mode: 'no-cors', body: data })
        .then(finish)
        .catch(function () {
          button.disabled = false;
          button.textContent = 'Try again';
          errorBox.textContent = 'Something went wrong sending your answers. Please check your connection and try again, or use the backup form below.';
          errorBox.hidden = false;
        });
    });
  }

  document.querySelectorAll('.lb-form').forEach(init);
})();
