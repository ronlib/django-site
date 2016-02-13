function getLastInput() {
		table  = $('#new_question_answers_table')[0];

}

function addOption() {
		if (!this.questionCount) {
				this.questionCount = 1;
		}

		var formTable  = $('#new_question_answers_table')[0];

		// One of the elements is the question text
		// var this.questionCount = formTable.getElementsByTagName('input').length - 1;

		var newOption = document.getElementById('id_question1').cloneNode(true);
		newOption.getElementsByTagName('td')[0].innerText =
				'Option ' + (this.questionCount + 1).toString();
		var newOptionInput = newOption.getElementsByTagName('input')[0];
		newOptionInput.type = 'text';
		newOptionInput.name = 'option' + (this.questionCount + 1).toString();
		newOptionInput.id = "id_question" + (this.questionCount + 1).toString();

		++this.questionCount;
		formTable.appendChild(newOption);
}

function handleInputChange(obj) {

		if (obj.value) {
				addOption();
		}
		else {
				// We should remove the next option, if it is not empty
				removeNextQuestionIfEmpty(obj);
		}

}

function getNextTr(obj) {
		return parentTr.parent().children()[parentTr.index()+1];
}

function removeNextQuestionIfEmpty(obj) {
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

		return nil;
}
