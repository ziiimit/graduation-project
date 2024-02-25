<template>
    <div id="search-result">
        <Loading v-if="loadingVisible" />
        <div v-else>
            <HomeBtn />
            <Response :userInput_zh="userInput_zh" :response_zh="response_zh" />
            <!-- <RecommendedArticleList :recommendedArticleList="recommendedArticleList" /> -->
        </div>
    </div>
</template>
<script>
import Loading from "@/components/Loading.vue";
import HomeBtn from "@/components/HomeBtn.vue";
import Response from "./components/Response.vue";
import RecommendedArticleList from "./components/RecommendedArticleList.vue"
import { getSearchResult } from "@/api/search.js";

export default {
    name: "SearchResult",
    components: { Loading, Response, HomeBtn, RecommendedArticleList },
    data() {
        return {
            userInput_zh: this.$route.query['userInput_zh'],
            response_zh: "",
            recommendedArticleList: [],
            loadingVisible: true
        }
    },
    created() {
        // getSearchResult(this.userInput_zh).then(res => {
        // console.log(res)
        let res = {
            "paragraphList": [
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "Categories of OCD",
                    "articleTitle_zh": "强迫症的类别",
                    "paragraphText_en": "Repetition obsessions and compulsions often overlap with checking behaviors and can involve activities like counting or repeating phrases or actions a specific number of times. This type of OCD can manifest in various ways, as seen in an example involving a band member who felt the need to walk up and down stairs a certain number of times before being satisfied. These repetitive behaviors, while seeming irrational to others, are significant manifestations of OCD that can significantly impact an individual's daily life.",
                    "score": 0.8642467260360718,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                },
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "Categories of OCD",
                    "articleTitle_zh": "强迫症的类别",
                    "paragraphText_en": "The third category of OCD is centered around order, which encompasses not only cleanliness and organization but also a fixation on completeness, symmetry, and disgust or contamination. Individuals with OCD related to order may feel a constant need to ensure that things are arranged perfectly or feel extreme discomfort when faced with perceived imperfections or asymmetry. This type of OCD can be particularly challenging as it can manifest in various settings and situations, leading individuals to constantly seek order and perfection in their surroundings.",
                    "score": 0.8569219708442688,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                },
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "Anxiety: Linking Obsessions & Compulsions",
                    "articleTitle_zh": "焦虑：将强迫症与强迫联系起来",
                    "paragraphText_en": "Furthermore, anxiety is a prevalent component in OCD, with up to 70% of individuals with OCD also experiencing elevated levels of anxiety. The relationship between OCD, anxiety, and depression is complex, as these conditions can be intertwined and exacerbate one another. OCD can lead to increased anxiety and depression, which can in turn worsen the symptoms of OCD. The interplay between these conditions underscores the importance of comprehensive treatment approaches that address both the obsessions and the anxiety that drives the compulsive behaviors.",
                    "score": 0.8455008268356323,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                },
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "Categories of OCD",
                    "articleTitle_zh": "强迫症的类别",
                    "paragraphText_en": "In conclusion, the categories of OCD - checking, repetition, and order obsessions and compulsions - offer a framework for understanding the diverse ways in which this disorder can manifest. By recognizing the different types of OCD behaviors and their impacts, we can gain insight into the complexity of this disorder and the challenges faced by individuals struggling to cope with its symptoms.",
                    "score": 0.8421049118041992,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                },
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "What is OCD and Obsessive-Compulsive Personality Disorder?",
                    "articleTitle_zh": "什么是强迫症和强迫性人格障碍？",
                    "paragraphText_en": "Obsessive-Compulsive Disorder (OCD) is a mental health condition characterized by intrusive and recurrent thoughts, known as obsessions, and repetitive behaviors or actions, known as compulsions. A key feature of OCD is the link between obsessions and compulsions, where the compulsions are often performed in an attempt to alleviate the anxiety or distress caused by the obsessions. However, unlike other behaviors that provide relief, compulsions in OCD tend to reinforce the obsessions, making them stronger over time. This pattern of behavior is essential in understanding and diagnosing OCD, as it distinguishes it from other mental health conditions.",
                    "score": 0.841943621635437,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                },
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "OCD & Familial Heredity",
                    "articleTitle_zh": "强迫症与家族遗传",
                    "paragraphText_en": "OCD, or Obsessive-Compulsive Disorder, has been a subject of interest regarding its potential familial heredity. The text mentions that there is indeed a genetic component to OCD, although the exact nature of it remains unclear. It is important to note that while some individuals may assume that if a condition is genetically influenced, it must be directly inherited from a parent, this is not always the case. Genes linked to OCD can manifest in siblings or children without being readily apparent in terms of phenotype, which is the observable characteristics like behavior patterns.",
                    "score": 0.8418188095092773,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                },
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "Cannabis CBD & Focus",
                    "articleTitle_zh": "大麻CBD和焦点",
                    "paragraphText_en": "In the case of OCD, where individuals experience intrusive thoughts and repetitive behaviors, the increased focus induced by cannabis CBD could potentially exacerbate symptoms. The text suggests that the relationship between anxiety, obsession, and compulsion in OCD may not align well with the increased focus provided by cannabis CBD. It is mentioned that the observed data did not show a worsening of OCD symptoms with cannabis CBD, which contradicts the initial assumption that heightened focus might intensify obsessions and compulsions.",
                    "score": 0.8411157727241516,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                },
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "Serotonin & Cognitive Flexibility, Psilocybin Studies",
                    "articleTitle_zh": "血清素与认知灵活性，Psilocybin研究",
                    "paragraphText_en": "The role of serotonin in cognitive flexibility and inflexibility, key elements of OCD, indirectly implicates this neurotransmitter in the disorder. Studies have shown that animals with depleted serotonin levels exhibit cognitive inflexibility, highlighting the potential influence of serotonin on cognitive functioning. Additionally, the impact of serotonin on the cortico-striatal-thalamic loop, a central system involved in OCD, further underscores the intricate relationship between serotonin and the manifestations of OCD symptoms. While the direct causal relationship between serotonin levels and OCD remains unclear, treatments like SSRIs and cognitive behavioral therapy have been shown to reduce OCD symptoms by modulating activity in the cortico-striatal-thalamic loop.",
                    "score": 0.8382909297943115,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                },
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "What is OCD and Obsessive-Compulsive Personality Disorder?",
                    "articleTitle_zh": "什么是强迫症和强迫性人格障碍？",
                    "paragraphText_en": "It is crucial to differentiate OCD from Obsessive-Compulsive Personality Disorder (OCPD), as they are distinct conditions. While OCD is characterized by intrusive and unwanted obsessions that trigger compulsions, OCPD revolves around a pattern of behavior where individuals derive satisfaction from their compulsive actions. Unlike in OCD, where the obsessions are distressing and unwanted, individuals with OCPD may find comfort and fulfillment in their compulsive behaviors, as they align with their desired way of functioning in the world. OCPD is more about a sense of delayed gratification and adherence to particular patterns of behavior that individuals perceive as enhancing their performance or presentation in society.",
                    "score": 0.8368996381759644,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                },
                {
                    "articleSetTitle_en": "The Science & Treatment of Obsessive Compulsive Disorder (OCD)",
                    "articleSetTitle_zh": "强迫症的科学与治疗",
                    "articleTitle_en": "OCD: Major Incidence & Severity",
                    "articleTitle_zh": "强迫症：主要发病率和严重程度",
                    "paragraphText_en": "In conclusion, OCD is a pervasive and severe mental health condition that affects a substantial portion of the population. The secrecy and shame associated with the disorder, coupled with its debilitating effects on daily functioning, underscore the urgent need for increased awareness, understanding, and support for individuals living with OCD. Addressing the incidence and severity of OCD requires destigmatization, early intervention, and access to appropriate mental health resources to help individuals manage their symptoms and improve their quality of life.",
                    "score": 0.8368381261825562,
                    "themeTitle_en": "Mental Health and Addiction",
                    "themeTitle_zh": "心理健康与成瘾"
                }
            ],
            "response_en": "Obsessive-Compulsive Disorder (OCD) is a mental health condition characterized by intrusive and recurrent thoughts, known as obsessions, and repetitive behaviors or actions, known as compulsions. People with OCD often experience intense anxiety or distress from their obsessions, which can range from intrusive thoughts to fears of contamination. In an attempt to alleviate this anxiety, individuals engage in compulsive behaviors or rituals that temporarily reduce the discomfort but ultimately reinforce the obsessions. This pattern of behavior distinguishes OCD from other mental health conditions, as the compulsions are performed to neutralize or prevent the feared consequences of the obsessions. OCD can significantly impact daily life and relationships, and comprehensive treatment approaches are essential to help individuals manage their symptoms and improve their quality of life.",
            "response_zh": "强迫症（OCD）是一种以入侵性和反复出现的想法（被称为强迫观念）以及重复的行为或动作（被称为强迫行为）为特征的精神健康状况。患有OCD的人经常因他们的强迫观念而经历强烈的焦虑或困扰，这些观念可以从入侵性思维到对污染的恐惧等各种形式。为了缓解这种焦虑，个体会参与强迫性行为或仪式，这些行为暂时减轻了不适，但最终会加强这些强迫观念。这种行为模式区分了OCD和其他精神健康状况，因为这些强迫行为是为了中和或预防强迫观念所引起的恐惧后果。OCD可以显著影响日常生活和人际关系，全面的治疗方法对于帮助个体管理症状并改善生活质量至关重要。"
        }
        this.response_zh = res['response_zh']
        for (let para of res['paragraphList']) {
            let currentArticleTitle_en = para['articleTitle_en']
            let exists = false
            for (let item of this.recommendedArticleList) {
                if (item['articleTitle_en'] == currentArticleTitle_en) {
                    exists = true;
                    break;
                }
            }
            if (!exists) {
                this.recommendedArticleList.push(para)
            }
        }
        this.loadingVisible = false;
        // }).catch(err => {

        // })
    }
}
</script>
<style scoped lang='scss'>
#search-result {
    padding-top: 80px;
}
</style>
