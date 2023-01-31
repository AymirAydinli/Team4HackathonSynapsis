'use client';
import { Inter } from '@next/font/google'
import { useRouter } from 'next/navigation';


const inter = Inter({ subsets: ['latin'] })


export async function getServerSideProps(context){


    const res = await fetch(`http://127.0.0.1:8000/api/FollowUpQuestionList/?questionare_id=${context.query.questionare_id}`);
    const data = await res.json();

    return {
      props: {questions: data, query: context.query}
  }}


export default function followUp({questions, query}) {
  const router = useRouter();
  console.log(query.questionare_id)

  const handleSubmit = (e) => {
    e.preventDefault()

    try{
      const respons = fetch(`http://127.0.0.1:8000/api/survey_injecttor_follow_up/?questionare_id=${query.questionare_id}`, {
        method: 'POST',
        body: JSON.stringify({"base_form_data":
            {
                "id": 1,
                "question": "Jaka jest reakcja dziecka?",
                "answer": false,
                "answer_value": false,
                "custom_answer":"blabla"
            }
        
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      }).then(res=>res.json()).then(response=>{
        console.log(response) })
    }
    catch{
      console.log("POST error")
    }
    
    console.log("SUBMIT")
    router.push('/')
    
    
    }

  return (
    <main className="flex item-center justify-center m-10">

      <div>
      
        <h1 className="mt-6 text-center text-lg md:text-3xl lg:text-3xl font-extrabold text-gray-900 py-12 px-4 sm:px-0 lg:px-0 ">
          Wypełnij wszystkie pola
        </h1>
        <form onSubmit={handleSubmit}  className="max-w-xs text-xs md:text-lg lg:text-lg  md:max-w-4xl lg:max-w-4xl ">

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
        </form>
      </div>

    </main>
  )
}
