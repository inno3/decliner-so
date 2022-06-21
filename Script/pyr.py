import math
import pyshs
from pandas.api.types import is_numeric_dtype
from sklearn.cluster import KMeans
import pandas as pd

# Author : Émilien Schultz

__version__ = "0.0.1"

def consolidation(X,clust,max_iter=10,**kwargs):
    """
    Apply a kmeans clustering on a MCA decomposition 
    using the centers of an hierarchical classification (HCPC)
    
    Parameters
    ----------
    X : DataFrame
        Table with the ACM dimensions and a column for the clusters
    clust : str
        Name of the cluster column
    max_inter : int
        Number of iterations
        
    Returns
    -------
    array
        New clusters with the same index
    
    """
    centers = X.groupby(clust).mean() # Calculer les centres
    km = KMeans(n_clusters = centers.shape[0], init=centers, max_iter=max_iter,**kwargs)
    new_clusters = km.fit_predict(X.drop(columns=clust))
    return new_clusters

def catdes(donnees,vardep,proba = 0.05, poids=False, modalites=False):
    """
    Calcule la dépendance entre une variable catégorielle et les autres variables catégorielles
    d'un tableau pour ne garder que celles significatives
    (testé vs. R, même résultats pour la pvalue)   
    """
    # Que les colonnes catégorielles
    cols = [c for c in donnees.columns if not is_numeric_dtype(donnees[c]) and c != vardep]
    
    # Boucle sur les colonnes
    results = []
    for v in cols:
        # Calcul du tableau croisé
        t,a,p = pyshs.tableau_croise(donnees,vardep,v,weight=poids,debug=True)
        a = a.drop(index="All",columns="All")
        
        # Calcul des statistiques sur le tableau d'effectif
        k,p,df,t = pyshs.chi2_contingency(a,correction=False) #testé avec R, même résultat
        
        # Garder les associations significatives
        if p < proba:
            results.append([v,p,df])
    
    # Mettre en forme le tableau
    results = pd.DataFrame(results,columns = [vardep,"p","df"]).set_index(vardep)
    results = results.sort_values("p")
    
    # Ajouter potentiellement le traitement des modalités individuelles
    if not modalites:   
        return results
    
    # Fonction dédiée (ci-dessous)
    if modalites:
        if not poids:
            supp = [vardep]
        else:
            supp = [vardep,poids]
        tableau_modalites = catdes_modalites(donnees[list(results.index)+supp],vardep,poids=poids)
        return results,tableau_modalites

def catdes_modalites(data,vardep,poids=False):
    """
    BETA BETA BETA
    Calcul par modalité des associations
    Notamment avec le v.test de catdes
    Attention : résultats un petit peu différent de R (quelques décimales)
    """
    
    if poids:
        print("Pas implémenté avec pondération")
        return None
    
    tableau = data.copy() # copie du tableau initial
    tab_dependantes = pd.get_dummies(tableau[[vardep]]) # passage en indicatrices 0/1
    tab_independantes = pd.get_dummies(tableau.drop(columns=vardep)) # passage des autres en indicatrices 0/1
    tab_all = pd.get_dummies(tableau) # tableau complet en dummies

    resultats = {}
    for categorie in tab_dependantes.columns:
        res_cat = []
        for modalite in tab_independantes.columns:
            
            t,a,p = pyshs.tableau_croise(tab_all.fillna(0),categorie,modalite,debug=True)
            xq = a.loc[1,1]/a.loc[1,"All"] #proportion de la variable par rapport à la catégorie
            x = a.loc["All",1]/a.loc["All","All"] #proportion de la variable par rapport à la population
            s = tab_independantes[modalite].std() #non pondéré attention
            Iq = a.loc[1,"All"]
            I = a.loc["All","All"]

            xc = a.loc[1,1]/a.loc["All",1] #proportion de la variable par rapport à la catégorie

            vtest = (xq-x)/(s*math.sqrt((1/Iq)*(I-Iq)/(I-1)))
            
            res_cat.append([modalite,100*xc,100*xq,100*x,vtest])
        resultats[categorie]= pd.DataFrame(res_cat,columns=["var dep",
            "cla/mod","mod/cla","Global","vtest"]).sort_values("vtest",ascending=False).set_index("var dep")
    #resultats = pd.concat(resultats)
    return resultats