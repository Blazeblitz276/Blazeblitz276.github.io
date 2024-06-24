skill_col_size = 5

# publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
                I am a passionate Data Scientist with a strong background in Electrical and Electronics Engineering, currently pursuing a Master's in Data Science at Indiana University Bloomington.
                **I believe in the power of data to drive decision-making and am skilled in both technical and analytical aspects of data science.**
              """,
        'name':'Balajee Devesha Srinivasan', 
        'study':'Indiana University Bloomington',
        'location':'Bloomington, IN',
        'interest':'Data Science, Machine Learning, Computer Vision',
        'skills':['Python', 'R', 'C', 'SQL', 'MATLAB', 'Numpy', 'Pandas', 'Scikit-Learn', 'TensorFlow', 'OpenCV', 'PySpark', 'Tidyverse', 'ggplot2', 'Langchain', 'boto3', 'Streamlit', 'ANN', 'NLP', 'LLM', 'Transformers', 'RAG', 'FAISS', 'Airflow', 'Kafka', 'AWS (S3, EC2, Lambda, SageMaker, Bedrock, RDS)', 'Git', 'Docker', 'Tableau', 'Power BI'],
        }

# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#[[header, subheader, date, location, content, link, link_url], [...], etc.]

Experience = [
              [":blue[Independent Researcher] | Computer Vision Dept, IUB", "Independent Researcher", 
              "January 2024 – May 2024", "Bloomington, IN", 
              """
              - Implemented advanced models to predict and generate intermediate frames, significantly improving video clarity using **GANs** and optical flow estimation.
              - Designed models to enhance video quality by accurately predicting and synthesizing intermediate frames, trained on SLURM-based HPC.
              - Enhanced model accuracy by 10% through tuning of neural network architectures and parameters, improving PSNR values by 20%.
              """,
              "Department website", "https://cs.indiana.edu/"] ,

              [":violet[Bosch Global Software Technologies Private Limited]", "Software Engineer", 
                "August 2019 – May 2022", "Bengaluru, India", 
                """
                - Investigated trends, patterns, and associations in IC-Engine knocking using Python and Scikit-learn, developing a machine learning model which led to a 25% reduction in knocking.
                - Constructed interactive data dashboards with Tableau to convey insights and model performances to stakeholders.
                - Collaborated with cross-functional teams to integrate data analytics solutions using SQL into existing systems, reducing overall time to deliver by 25%.
                - Spearheaded end-to-end analysis of requirements, conducted code reviews, and managed software integrations, guaranteeing on-time deliveries and boosting operational excellence by 20%.
                """,
                "Company website", "https://www.bosch.com"]      
              ]      

# Portfolio --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     {'project1':[HEADER, CONTENT]
#      'project2':[HEADER, CONTENT]
#      ...}

Portfolio = { 1:[':blue[Hurricane Intensity Prediction] - Computer Vision Project',
              """
              Developed a Hurricane/Cyclone Intensity Prediction model using a CNN with TensorFlow, leveraging raw images from HURSAT and INSAT datasets for per-class classification, achieving a 92% accuracy rate. Devised an ensemble of CNN classifiers to enhance the model’s performance, resulting in a 15% increase in accuracy compared to the single model approach.
              """],
              2:['Stellar Data Classification in :orange[PySpark]',
                  """
                Boosted data processing by 30% with PySpark’s distributed processing and amplified feature engineering of SDSS observations dataset, uncovering correlations and patterns among celestial objects deployed on HPC instance. Created a multi-algorithmic machine learning and deep learning classification ETL pipeline using PySpark on a Linux cloud, achieving 95% accuracy in classifying celestial objects and reducing processing time by 30%.
                """],
              3:[':blue[LLM Desktop ChatApp]',
                """
                - Engineered an intelligent PDF chatbot utilizing AWS S3, Bedrock, and FAISS for efficient document querying, enhancing real-time data retrieval and interactive user experience with server and client deployed using Docker.
                - Devised a scalable end-to-end machine learning pipeline on AWS, incorporating the Llama 70B model for natural language processing and dynamic content extraction from PDFs.
                """],
              4:[':orange[Japanese Restaurant Visitor Forecasting]',
                """
                - Analyzed visitor trends in Japanese restaurants utilizing the "Recruit Restaurant Visitor Forecasting" dataset from Kaggle, discovering insights and modeling data from over 13,000 restaurants. Investigated using time series modeling in R to identify the impact of seasonal variations and restaurant locations on visitor numbers, leading to a 20% improvement in forecasting accuracy using simpler models like loess, and GLM.
                """]
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phone = "+1(812) 778-0392"
email = "sbdevesha1998@gmail.com"
linkedin_link = "www.linkedin.com/in/balajeedeveshas/"
github_link = "https://github.com/Blazeblitz276"


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Blazeblitz276/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''

