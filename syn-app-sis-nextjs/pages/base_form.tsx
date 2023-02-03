import { useRouter } from 'next/navigation';
import Modal from '@/components/modal';

import React, { Fragment, useState } from "react";
import { type } from 'os';

export const getStaticProps = async () =>{
  const res = await fetch("http://127.0.0.1:8000/api/baseQuestionList/");
  const data = await res.json();

  return {
    props: {questions: data}
  }
}


const base_form = ({questions}: {questions:any}) => {
  //console.log(questions);

  const [showModal, setShowModal] = useState(false);
  const [questionareIdModal, setquestionareIdModal] = useState(0)
  let questionare_id = 0;

  const router = useRouter();

  const map_question_answer = (answers: Array<Event>) =>
  {
    
    let mapped_questions = {"answers":[]}
    let question_id = 0
    let score = 0
    let answer
    for(let idx = 0; idx < answers.length-1 ; idx++)
    {
      
      console.log("ID", idx)
      if(answers[idx].id.includes("yes")){
        console.log("yes")
      }
      if (answers[idx].checked == true) {
        if(answers[idx].id.includes("yes")) {
          answer = true
        }
        else{
          answer = false
        } 
        // we need to change scoring to opposite for some questions
        if (questions["questions"][question_id]["pass_choice"] == false ){
          answer = !answer
        }
        
        if (answer == false){
          score++
        }
        mapped_questions["answers"][questions["questions"][question_id]["id"]] = answer
        question_id++
      }    
    }
    mapped_questions["score"] = score
    return mapped_questions
  }


  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(e.target)
    let base_form_data = map_question_answer(e.target)

    let date_split = document.querySelector('#date').value.split("-", 3)
    base_form_data["post_code"] = document.querySelector('#code').value
    base_form_data["month_of_birth"] = date_split[1]
    base_form_data["year_of_birth"] = date_split[0]
    base_form_data["date_of_birth"] = document.querySelector('#date').value


    console.log(base_form_data)
    try{
      const respons = fetch("http://127.0.0.1:8000/api/survey_injector/", {
        method: 'POST',
        body: JSON.stringify({base_form_data}),
        headers: {
          'Content-Type': 'application/json',
        },
      }).then(res=>res.json()).then(response=>{
        console.log(response); 
        questionare_id = response["questioner_id"]

        console.log("AAAAA", questionare_id)
        if(base_form_data["score"] <=2){
          setShowModal(true)
          setquestionareIdModal(questionare_id)
        }
        else{
         router.push({
            pathname:'/follow_up/[questionare_id]', 
            query:{ questionare_id: questionare_id }
        })
        }

      })
    }
    catch{
      console.log("POST error")
    }
  }

  return (
    <main className="flex item-center justify-center m-10">

      <div>
      
        <h1 className="mt-6 text-center text-lg md:text-3xl lg:text-3xl font-extrabold text-gray-900 py-12 px-4 sm:px-0 lg:px-0 ">
          Wypełnij wszystkie pola
        </h1>
        <form onSubmit={handleSubmit}  className="max-w-xs text-xs md:text-lg lg:text-lg  md:max-w-4xl lg:max-w-4xl ">
        <Fragment>
        <div className="flex flex-col md:flex-row lg:flex-row lg:items-center mb-4 space-x-3" >
          <label className="flex  flex-row ml-2 text-xs md:text-sm lg:text-sm font-medium text-gray-900 dark:text-gray-300">Kod pocztowy</label>
          <input type="text" id="code" name="code" className=" inline-flex items-center border-2"required />
          <label className="ml-2 text-xs md:text-sm lg:text-sm font-medium text-gray-900 dark:text-gray-300">Data urodzenia</label>
          <input type="date" id="date" name="date"  className="inline-flex items-center border-2 "required />
        </div>
          {questions["questions"].map(question => (
            <div className='border-2 rounded-md py-2 px-4 sm:px-6 lg:px-8 bg-slate-50' key={question.id} >
              <a>
                <h3>{question.question_no}. {question.question_text_pl}</h3>
              </a>
          
          <div className=" flex items-center mb-4 space-x-3 rounded-md " >
            <input type="radio" name={question.id} id={"yes"+question.id} className="inline-flex items-center"required/> 
              <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Tak</label>
            <input type="radio"name={question.id} id={"no"+question.id} className="inline-flex items-center " required/> 
              <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Nie</label>
          </div>
            </div>
          ))

          }
          <input type='submit'
            className="group relative flex-center justify-center
            py-2 px-4 border border-transparent text-sm font-medium
            rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
            value='Zakończ ankietę' 
          />
          <Modal isVisible={showModal} questionare_id={questionareIdModal}></Modal>
          </Fragment>
        </form>
      </div>

    </main>
  );
};
  
export default base_form;