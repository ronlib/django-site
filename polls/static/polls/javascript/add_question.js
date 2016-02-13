function getLastInput() {
		table  = $('#new_question_answers_table')[0];

}

function addOption() {
		if (!this.questionCount) {
				this.questionCount = 1;
		}

		var newOption = $(".answer-template").children()[0].cloneNode(true);

		$(newOption).find("label").attr("for", 'answerText' + this.questionCount.toString());
		$(newOption).find("input").attr("id", 'answerText' + this.questionCount.toString());

		++this.questionCount;
		$("#newQuestion")[0].appendChild(newOption);

}

function isLastInput(obj) {

		if ($(obj).siblings().length == $(obj).index()) {
				return true;
		}

		return false;
}

function handleInputChange(obj) {

		var formGroup = $(obj).parents(".form-group");

		if (obj.value && isLastInput(formGroup)) {
				addOption();
		}
		else if (!isLastInput(formGroup) && !obj.value) {
				// We should remove the next option, if it is not empty
				$(formGroup.parent().children()[formGroup.index()-1]).find("input")[0].focus();
				formGroup.remove();
		}

}

function getNextTr(obj) {
		return parentTr.parent().children()[parentTr.index()+1];
}
