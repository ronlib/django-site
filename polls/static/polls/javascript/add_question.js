function getLastInput() {
		table  = $('#new_question_answers_table')[0];

}

function addOption() {
		formTable  = $('#new_question_answers_table')[0];

		// One of the elements is the question text
		numberOfInputs = formTable.getElementsByTagName('input').length - 1;

		newOption = document.getElementById('id_question1').cloneNode();
		newOption.getElementsByTagName('td')[0] =
				'Option ' + (numberOfInputs + 1).toString();
		newOptionInput = newOption.getElementsByTagName('input')[0];
		newOptionInput.type = 'text';
		newOptionInput.name = 'option' + (numberOfInputs + 1).toString();
		newOptionInput.id = "id_question" + (numberOfInputs + 1).toString();

		formTable.appendChild(newOption);
}
