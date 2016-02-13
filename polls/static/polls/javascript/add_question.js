function getLastInput() {
		table  = $('#new_question_answers_table')[0];

}

function addOption() {
		formTable  = $('#new_question_answers_table')[0];

		// One of the elements is the question text
		numberOfInputs = formTable.getElementsByTagName('input').length - 1;

		newOption = document.getElementById('id_question1').cloneNode(true);
		newOption.getElementsByTagName('td')[0].innerText =
				'Option ' + (numberOfInputs + 1).toString();
		newOptionInput = newOption.getElementsByTagName('input')[0];
		newOptionInput.type = 'text';
		newOptionInput.name = 'option' + (numberOfInputs + 1).toString();
		newOptionInput.id = "id_question" + (numberOfInputs + 1).toString();

		formTable.appendChild(newOption);
}


function isNextOptionFilled(obj) {

		if (obj.value) {
				addOption();
		}
		else {
				// We should remove the next option, if it is not empty
				obj.parentElement().parentElement();
		}

}

function getNextQuestion(obj) {
		parentTr = $(obj.parentElement.parentElement);
		if (parentTr.siblings().length == parentTr.index()) {
				// Last element
				return nil;
		}
		else {
				nextTr = parentTr.parent().children()[parentTr.index()+1];
				if (!nextTr.value) {
						nextTr.remove();
				}
		}
}
