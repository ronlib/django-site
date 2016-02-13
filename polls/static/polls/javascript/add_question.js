function getLastInput() {
		table  = $('#new_question_answers_table')[0];

}

function addOption() {
		if (!this.questionCount) {
				this.questionCount = 1;
		}

		var formTable  = $('#new_question_answers_table>tbody')[0];

		// One of the elements is the question text
		// var this.questionCount = formTable.getElementsByTagName('input').length - 1;

		var newOption = document.getElementById('id_question1').cloneNode(true);
		newOption.getElementsByTagName('td')[0].innerText =
				'Option ' + (this.questionCount + 1).toString();
		var newOptionInput = newOption.getElementsByTagName('input')[0];
		newOptionInput.type = 'text';
		newOptionInput.name = 'option' + (this.questionCount + 1).toString();
		newOptionInput.id = "id_question" + (this.questionCount + 1).toString();
		newOptionInput.value = "";

		++this.questionCount;
		formTable.appendChild(newOption);
}

function isLastInput(obj) {

		if (obj.siblings().length == obj.index()) {
				return true;
		}

		return false;
}

function handleInputChange(obj) {

		trElement = $(obj).parent().parent();

		if (obj.value && isLastInput(trElement)) {
				addOption();
		}
		else if (!isLastInput(trElement) && !obj.value) {
				// We should remove the next option, if it is not empty
				$(trElement.parent().children()[trElement.index()-1]).find("input")[0].focus();
				trElement.remove();
		}

}

function getNextTr(obj) {
		return parentTr.parent().children()[parentTr.index()+1];
}
