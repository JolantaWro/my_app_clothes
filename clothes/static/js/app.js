document.addEventListener("DOMContentLoaded", function() {
/**
 * HomePage - Help section
 */
class Help {
  constructor($el) {
    this.$el = $el;
    this.$buttonsContainer = $el.querySelector(".help--buttons");
    this.$slidesContainers = $el.querySelectorAll(".help--slides");
    this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
    this.init();
  }

  init() {
    this.events();
  }

  events() {
    /**
     * Slide buttons
     */
    this.$buttonsContainer.addEventListener("click", e => {
      if (e.target.classList.contains("btn")) {
        this.changeSlide(e);
      }
    });

    /**
     * Pagination buttons
     */
    this.$el.addEventListener("click", e => {
      if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
        this.changePage(e);
      }
    });
  }

  changeSlide(e) {
    e.preventDefault();
    const $btn = e.target;

    // Buttons Active class change
    [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
    $btn.classList.add("active");

    // Current slide
    this.currentSlide = $btn.parentElement.dataset.id;


    // Slides active class change
    this.$slidesContainers.forEach(el => {
      el.classList.remove("active");

      if (el.dataset.id === this.currentSlide) {
        el.classList.add("active");
      }
    });
  }

  /**
   * TODO: callback to page change event
   */
  changePage(e) {
    e.preventDefault();
    const page = e.target.dataset.page;
  }
}
const helpSection = document.querySelector(".help");
if (helpSection !== null) {
  new Help(helpSection);
}

/**
 * Form Select
 */
class FormSelect {
  constructor($el) {
    this.$el = $el;
    this.options = [...$el.children];
    this.init();
  }

  init() {
    this.createElements();
    this.addEvents();
    this.$el.parentElement.removeChild(this.$el);
  }

  createElements() {
    // Input for value
    this.valueInput = document.createElement("input");
    this.valueInput.type = "text";
    this.valueInput.name = this.$el.name;

    // Dropdown container
    this.dropdown = document.createElement("div");
    this.dropdown.classList.add("dropdown");

    // List container
    this.ul = document.createElement("ul");

    // All list options
    this.options.forEach((el, i) => {
      const li = document.createElement("li");
      li.dataset.value = el.value;
      li.innerText = el.innerText;

      if (i === 0) {
        // First clickable option
        this.current = document.createElement("div");
        this.current.innerText = el.innerText;
        this.dropdown.appendChild(this.current);
        this.valueInput.value = el.value;
        li.classList.add("selected");
      }

      this.ul.appendChild(li);
    });

    this.dropdown.appendChild(this.ul);
    this.dropdown.appendChild(this.valueInput);
    this.$el.parentElement.appendChild(this.dropdown);
  }

  addEvents() {
    this.dropdown.addEventListener("click", e => {
      const target = e.target;
      this.dropdown.classList.toggle("selecting");

      // Save new value only when clicked on li
      if (target.tagName === "LI") {
        this.valueInput.value = target.dataset.value;
        this.current.innerText = target.innerText;
      }
    });
  }
}
document.querySelectorAll(".form-group--dropdown select").forEach(el => {
  new FormSelect(el);
});

/**
 * Hide elements when clicked on document
 */
document.addEventListener("click", function(e) {
  const target = e.target;
  const tagName = target.tagName;

  if (target.classList.contains("dropdown")) return false;

  if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
    return false;
  }

  if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
    return false;
  }

  document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
    el.classList.remove("selecting");
  });
});

/**
 * Switching between form steps
 */
class FormSteps {
  constructor(form) {
    this.$form = form;
    this.$next = form.querySelectorAll(".next-step");
    this.$prev = form.querySelectorAll(".prev-step");
    this.$step = form.querySelector(".form--steps-counter span");
    this.currentStep = 1;

    this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
    const $stepForms = form.querySelectorAll("form > div");
    this.slides = [...this.$stepInstructions, ...$stepForms];
    const choiceElement = form.querySelectorAll("#choice");
    this.selectedCategories = [];
    this.selectedInstitution = "";
    this.nextBtn = form.querySelector(".active .next-step")
    this.nextBtn.style.display = "none"
    this.errorForm = form.querySelector(".errorFormText")


    choiceElement.forEach((element) => {
      element.addEventListener("click", (event) => {
        if (element.checked) {
          this.selectedCategories.push(event.target.value)
          this.nextBtn.style.display = "block"
        } else {
          this.selectedCategories = this.selectedCategories.filter( cat => cat === event.target.value)
        }
      })
    })
    this.init();
  }

  /**
   * Init all methods
   */
  init() {
    this.events();
    this.updateForm();
  }

  /**
   * All events that are happening in form
   */
  events() {
    // Next step
    this.$next.forEach(btn => {
      btn.addEventListener("click", e => {
        e.preventDefault();
        this.currentStep++;
        this.updateForm();
      });
    });

    // Previous step
    this.$prev.forEach(btn => {
      btn.addEventListener("click", e => {
        e.preventDefault();
        this.currentStep--;
        this.updateForm();
      });
    });

    // Form submit
    this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
  }

  /**
   * Update form front-end
   * Show next or previous section etc.
   */
  updateForm() {
    this.$step.innerText = this.currentStep;
    this.institutionElements = document.querySelectorAll("#institution");



    // TODO: Validation

    this.slides.forEach(slide => {
      slide.classList.remove("active");

      if (Number(slide.dataset.step) === this.currentStep) {
        slide.classList.add("active");
      }
    });

    if (this.currentStep === 3) {
      this.bugs = document.querySelector('#bags').value
      if (this.bugs === "0") {
        this.errorForm.style.display = "block"
      }

      this.institutionElements.forEach( (elementDiv) => {
        const institutionCategories = elementDiv.dataset.id.split(" ")
        if (this.selectedCategories.some(selectedCategory => institutionCategories.includes(selectedCategory))) {
          elementDiv.style.display = "block"
        } else {
          elementDiv.style.display = "none"
        }
      })

      const choiceInstitution = document.querySelectorAll("#institution_choice");
      choiceInstitution.forEach(element => {
        element.addEventListener("click", (event) => {
          if (element.checked) {
            this.selectedInstitution = event.target.value
          }
        })
      })
    }

    this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
    this.$step.parentElement.hidden = this.currentStep >= 6;


    // TODO: get data from inputs and show them in summary

    const showInputValue = (value, element) => {
      if (value !== "") {
        element.innerText = value
      } else {
        element.innerText = 'Nie wprowadzono informacji'
        this.errorForm.style.display = "block"
      }
    }
    if (this.currentStep === 5) {

      const streetValue = document.querySelector('#street').value
      const cityValue = document.querySelector('#city').value
      const postcodeValue = document.querySelector('#postcode').value
      const phoneValue = document.querySelector('#phone').value
      const dataValue = document.querySelector('#data').value
      const timeValue = document.querySelector('#time').value
      const moreInfoValue = document.querySelector('#more_info').value
      // this.bugs = document.querySelector('#bags').value


      const spanBugs = document.querySelector('li.bag_view')
      const spanInstitution = document.querySelector('li.institution_view')
      const spanStreet = document.querySelector('li.street_view')
      const spanCity = document.querySelector('li.city_view')
      const spanPostcode = document.querySelector('li.postcode_view')
      const spanPhone = document.querySelector('li.phone_view')
      const spanData = document.querySelector('li.data_view')
      const spanTime = document.querySelector('li.time_view')
      const spanInfo = document.querySelector('li.more_info_view')

      if (this.bugs !== "0") {
        this.errorForm.style.display = "none"
      }

      showInputValue(streetValue, spanStreet)
      showInputValue(cityValue, spanCity)
      showInputValue(postcodeValue, spanPostcode)
      showInputValue(phoneValue, spanPhone)
      showInputValue(dataValue, spanData)
      showInputValue(timeValue, spanTime)
      spanInfo.innerText = moreInfoValue
      spanBugs.innerHTML = `<span class="icon icon-bag"></span><span class="summary--text">${this.bugs }</span>`
      spanInstitution.innerHTML = `<span class="icon icon-hand"></span><span class="summary--text">Dla ${this.selectedInstitution}</span>`
    }
  }

  /**
   * Submit form
   *
   * TODO: validation, send data to server
   */
  submit(e) {
    // e.preventDefault();
    this.currentStep++;
    this.updateForm();
  }
}
const form = document.querySelector(".form--steps");

if (form !== null) {
  new FormSteps(form);
}

});

