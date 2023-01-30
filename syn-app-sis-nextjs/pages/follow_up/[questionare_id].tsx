'use client';
import { Inter } from '@next/font/google'
import { useRouter } from 'next/navigation';
import { GetStaticPaths} from 'next'


const inter = Inter({ subsets: ['latin'] })

export const getStaticProps = async () =>{
    const res = await fetch("http://127.0.0.1:8000/api/FollowUpQuestionList/");
    const data = await res.json();
  
    return {
      props: {questions: data}
    }
  }

  export const getStaticPaths: GetStaticPaths = async () =>{
    return {
      
      paths: [
        { params: { questionare_id: 'questionare_id' } },
      ],
      fallback: true,
    }
  }
export default function followUp({questions, params}) {
  const router = useRouter();
  console.log("ROUTER ID", router.asPath);

  const handleSubmit = (e) => {
    e.preventDefault()
    
    console.log("QUEST ID",params)
    console.log("SUBMIT")
    router.push('/')
    
    
    }

  return (
    <main className=" w-screen flex item-center justify-center m-10">

      <div>
      
        <h1 className="mt-6 text-center text-3xl font-extrabold text-gray-900 py-12 px-4 sm:px-6 lg:px-8 ">
          Wypełnij wszystkie pola
        </h1>
        <form onSubmit={handleSubmit} >

          {questions["questions"].map(question => (
            <div className='border-2 py-2 px-4 sm:px-6 lg:px-8' key={question.id} >
              <a>
                <h3>{question.question_no}. {question.question_text_pl}</h3>
              </a>
          
          <div className=" flex items-center mb-4 space-x-3 rounded-md" >
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
